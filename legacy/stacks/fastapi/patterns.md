# FastAPI Stack - Design Patterns

Patrones de diseño implementados en el stack FastAPI con ejemplos de código Python completos y funcionales.

## 1. Repository Pattern

Abstrae el acceso a datos. Los use cases no saben si es PostgreSQL, SQLite, o cualquier otro almacenamiento.

### BaseRepository con filtro automático

```python
# app/infrastructure/persistence/base_repository.py
from typing import TypeVar, Type, Generic, Optional, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_
from sqlalchemy.orm import DeclarativeBase

T = TypeVar('T', bound=DeclarativeBase)

class BaseRepository(Generic[T]):
    """Repository base con operaciones comunes y filtro de tenant/sucursal"""

    def __init__(self, db: AsyncSession, model: Type[T], sucursal_id: Optional[int] = None):
        self.db = db
        self.model = model
        self.sucursal_id = sucursal_id

    async def find_by_id(self, id: int) -> Optional[T]:
        """Buscar por ID con filtro de sucursal si aplica"""
        query = select(self.model).where(self.model.id == id)
        query = self._filtrar(query)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def find_all(
        self,
        skip: int = 0,
        limit: int = 100,
        where_clauses: Optional[list] = None
    ) -> list[T]:
        """Listar con paginación y filtros opcionales"""
        query = select(self.model)
        query = self._filtrar(query)

        if where_clauses:
            query = query.where(and_(*where_clauses))

        query = query.offset(skip).limit(limit)
        query = query.order_by(self.model.id.desc())

        result = await self.db.execute(query)
        return result.scalars().all()

    async def count(self, where_clauses: Optional[list] = None) -> int:
        """Contar registros con filtros opcionales"""
        query = select(func.count(self.model.id))
        query = self._filtrar(query)

        if where_clauses:
            query = query.where(and_(*where_clauses))

        result = await self.db.execute(query)
        return result.scalar()

    async def save(self, entity: T) -> T:
        """Guardar (create o update)"""
        self.db.add(entity)
        await self.db.flush()
        await self.db.refresh(entity)
        return entity

    async def delete(self, id: int) -> bool:
        """Soft delete si existe deleted_at, hard delete si no"""
        entity = await self.find_by_id(id)
        if not entity:
            return False

        if hasattr(entity, 'deleted_at'):
            entity.deleted_at = datetime.utcnow()
            await self.db.flush()
        else:
            await self.db.delete(entity)

        return True

    def _filtrar(self, query):
        """Aplicar filtro de sucursal si el modelo tiene sucursal_id"""
        if self.sucursal_id and hasattr(self.model, 'sucursal_id'):
            return query.where(self.model.sucursal_id == self.sucursal_id)
        return query
```

### Implementación concreta: SQLAlchemyOrdenRepository

```python
# app/infrastructure/persistence/sqlalchemy_orden_repo.py
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from app.infrastructure.persistence.models import OrdenModel
from app.application.ports.orden_repository import AbstractOrdenRepository
from app.domain.entities.orden import Orden, OrdenEstado
from app.infrastructure.persistence.base_repository import BaseRepository

class SQLAlchemyOrdenRepository(BaseRepository[OrdenModel], AbstractOrdenRepository):
    """Implementación concreta de AbstractOrdenRepository usando SQLAlchemy"""

    def __init__(self, db: AsyncSession, sucursal_id: Optional[int] = None):
        super().__init__(db, OrdenModel, sucursal_id)

    async def save(self, orden: Orden) -> Orden:
        """Guardar orden mapeando desde entidad a modelo"""
        model = OrdenModel(
            numero=orden.numero,
            mesa_id=orden.mesa_id,
            cliente_id=orden.cliente_id,
            total=orden.total,
            estado=orden.estado.value,
            sucursal_id=orden.sucursal_id,
            created_at=datetime.utcnow()
        )

        self.db.add(model)
        await self.db.flush()
        await self.db.refresh(model)

        # Mapear items si existen
        if orden.items:
            for item in orden.items:
                item_model = OrdenItemModel(
                    orden_id=model.id,
                    producto_id=item.producto_id,
                    cantidad=item.cantidad,
                    precio_unitario=item.precio_unitario,
                    subtotal=item.subtotal
                )
                self.db.add(item_model)

        await self.db.commit()
        return self._to_entity(model)

    async def find_by_id(self, orden_id: int) -> Optional[Orden]:
        """Buscar orden por ID con sus items"""
        model = await super().find_by_id(orden_id)
        if not model:
            return None
        return self._to_entity(model)

    async def find_activas_por_mesa(self, mesa_id: int) -> list[Orden]:
        """Buscar órdenes activas de una mesa"""
        query = select(OrdenModel).where(
            and_(
                OrdenModel.mesa_id == mesa_id,
                OrdenModel.estado == OrdenEstado.ABIERTA.value
            )
        )
        query = self._filtrar(query)

        result = await self.db.execute(query)
        models = result.scalars().all()
        return [self._to_entity(m) for m in models]

    async def find_por_estado(
        self,
        estado: OrdenEstado,
        skip: int = 0,
        limit: int = 100
    ) -> list[Orden]:
        """Buscar órdenes por estado"""
        query = select(OrdenModel).where(OrdenModel.estado == estado.value)
        query = self._filtrar(query)
        query = query.offset(skip).limit(limit)

        result = await self.db.execute(query)
        models = result.scalars().all()
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: OrdenModel) -> Orden:
        """Mapear desde modelo de SQLAlchemy a entidad de dominio"""
        items = [
            OrdenItem(
                producto_id=item.producto_id,
                cantidad=item.cantidad,
                precio_unitario=item.precio_unitario,
                subtotal=item.subtotal
            )
            for item in model.items
        ]

        return Orden(
            id=model.id,
            numero=model.numero,
            mesa_id=model.mesa_id,
            cliente_id=model.cliente_id,
            items=items,
            total=model.total,
            estado=OrdenEstado(model.estado),
            sucursal_id=model.sucursal_id,
            created_at=model.created_at,
            updated_at=model.updated_at
        )
```

---

## 2. Factory Pattern

Crear objetos complejos con lógica de construcción encapsulada.

### TicketFactory para generar tickets de venta

```python
# app/domain/factories/ticket_factory.py
from dataclasses import dataclass
from typing import List
from app.domain.entities.orden import Orden
from app.domain.entities.config import TenantConfig

@dataclass
class TicketLinea:
    producto: str
    cantidad: int
    precio: float
    subtotal: float

@dataclass
class Ticket:
    numero: str
    fecha: str
    hora: str
    lineas: List[TicketLinea]
    subtotal: float
    iva: float
    total: float
    metodo_pago: str
    cajero: str
    cliente: str
    sucursal: str
    logo: str
    pie: str

class TicketFactory:
    """Factory para crear tickets desde órdenes con formato específico del tenant"""

    @staticmethod
    def crear_desde_orden(orden: Orden, config: TenantConfig, cajero_nombre: str) -> Ticket:
        """Crear ticket desde una orden con configuración del tenant"""
        from datetime import datetime

        ahora = datetime.now()

        # Crear líneas del ticket
        lineas = [
            TicketLinea(
                producto=f"{item.producto_nombre} ({item.descripcion})" if item.descripcion else item.producto_nombre,
                cantidad=item.cantidad,
                precio=item.precio_unitario,
                subtotal=item.subtotal
            )
            for item in orden.items
        ]

        # Calcular totales
        subtotal = sum(l.subtotal for l in lineas)
        iva = subtotal * 0.16  # 16% IVA México
        total = subtotal + iva

        # Determinar nombre del cliente
        cliente_nombre = orden.cliente_nombre if orden.cliente_nombre else "Cliente General"

        return Ticket(
            numero=orden.numero,
            fecha=ahora.strftime("%d/%m/%Y"),
            hora=ahora.strftime("%H:%M:%S"),
            lineas=lineas,
            subtotal=subtotal,
            iva=iva,
            total=total,
            metodo_pago=orden.metodo_pago.value,
            cajero=cajero_nombre,
            cliente=cliente_nombre,
            sucursal=config.sucursal_nombre,
            logo=config.logo_ticket,
            pie=config.pie_ticket
        )

    @staticmethod
    def crear_corte_caja(
        turno_caja,
        config: TenantConfig,
        cajero_nombre: str
    ) -> Ticket:
        """Crear ticket de corte de caja"""
        from datetime import datetime

        ahora = datetime.now()

        # Líneas del corte de caja
        lineas = [
            TicketLinea(
                producto="Efectivo inicial",
                cantidad=1,
                precio=turno_caja.fondo_inicial,
                subtotal=turno_caja.fondo_inicial
            ),
            TicketLinea(
                producto="Ventas efectivo",
                cantidad=1,
                precio=turno_caja.ventas_efectivo,
                subtotal=turno_caja.ventas_efectivo
            ),
            TicketLinea(
                producto="Ventas tarjeta",
                cantidad=1,
                precio=turno_caja.ventas_tarjeta,
                subtotal=turno_caja.ventas_tarjeta
            ),
            TicketLinea(
                producto="Retiros",
                cantidad=1,
                precio=-turno_caja.retiros,
                subtotal=-turno_caja.retiros
            ),
        ]

        total = turno_caja.fondo_inicial + turno_caja.ventas_efectivo + turno_caja.ventas_tarjeta - turno_caja.retiros

        return Ticket(
            numero=f"CORTE-{turno_caja.id}",
            fecha=ahora.strftime("%d/%m/%Y"),
            hora=ahora.strftime("%H:%M:%S"),
            lineas=lineas,
            subtotal=total,
            iva=0.0,
            total=total,
            metodo_pago="CORTE",
            cajero=cajero_nombre,
            cliente="---",
            sucursal=config.sucursal_nombre,
            logo=config.logo_ticket,
            pie=config.pie_ticket
        )
```

---

## 3. Strategy Pattern

Múltiples algoritmos intercambiables para el mismo problema.

### Estrategias de pago

```python
# app/domain/strategies/pago_strategy.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class MetodoPago(Enum):
    EFECTIVO = "efectivo"
    TARJETA = "tarjeta"
    TRANSFERENCIA = "transferencia"
    CHEQUE = "cheque"

@dataclass
class ResultadoPago:
    exitoso: bool
    mensaje: str
    referencia: Optional[str] = None
    cambio: float = 0.0
    comision: float = 0.0

class AbstractMetodoPago(ABC):
    """Estrategia base para métodos de pago"""

    @abstractmethod
    async def procesar(
        self,
        monto: float,
        monto_entregado: Optional[float] = None,
        metadata: Optional[dict] = None
    ) -> ResultadoPago:
        """Procesar el pago y retornar resultado"""
        pass

class PagoEfectivo(AbstractMetodoPago):
    """Estrategia de pago en efectivo"""

    async def procesar(
        self,
        monto: float,
        monto_entregado: Optional[float] = None,
        metadata: Optional[dict] = None
    ) -> ResultadoPago:
        if monto_entregado is None:
            return ResultadoPago(
                exitoso=False,
                mensaje="Debe especificar el monto entregado en efectivo"
            )

        if monto_entregado < monto:
            return ResultadoPago(
                exitoso=False,
                mensaje=f"Faltan ${monto - monto_entregado:.2f} para completar el pago"
            )

        cambio = monto_entregado - monto
        return ResultadoPago(
            exitoso=True,
            mensaje="Pago en efectivo recibido correctamente",
            cambio=cambio,
            comision=0.0
        )

class PagoTarjeta(AbstractMetodoPago):
    """Estrategia de pago con tarjeta (terminal bancario)"""

    def __init__(self, terminal_id: str):
        self.terminal_id = terminal_id

    async def procesar(
        self,
        monto: float,
        monto_entregado: Optional[float] = None,
        metadata: Optional[dict] = None
    ) -> ResultadoPago:
        # Aquí se integraría con el terminal bancario real
        # Por ahora simulamos una aprobación

        comision = monto * 0.035  # 3.5% comisión tarjeta

        # Simulación de llamada al terminal
        await self._procesar_terminal(monto, metadata)

        return ResultadoPago(
            exitoso=True,
            mensaje="Pago con tarjeta aprobado",
            referencia=f"TXN-{self.terminal_id}-{int(monto * 100)}",
            cambio=0.0,
            comision=comision
        )

    async def _procesar_terminal(self, monto: float, metadata: Optional[dict]):
        """Simular procesamiento en terminal bancario"""
        # En producción: integración con SDK del terminal (Verifone, Ingenico, etc.)
        import asyncio
        await asyncio.sleep(0.5)  # Simular latencia

class PagoTransferencia(AbstractMetodoPago):
    """Estrategia de pago por transferencia bancaria"""

    async def procesar(
        self,
        monto: float,
        monto_entregado: Optional[float] = None,
        metadata: Optional[dict] = None
    ) -> ResultadoPago:
        referencia = metadata.get('referencia') if metadata else None

        if not referencia:
            return ResultadoPago(
                exitoso=False,
                mensaje="Debe proporcionar la referencia de transferencia"
            )

        # Aquí se podría validar la referencia contra el banco
        return ResultadoPago(
            exitoso=True,
            mensaje="Pago por transferencia registrado (pendiente de confirmación)",
            referencia=referencia,
            cambio=0.0,
            comision=0.0
        )

class PagoStrategyFactory:
    """Factory para crear estrategias de pago"""

    @staticmethod
    def crear(metodo: MetodoPago, config: Optional[dict] = None) -> AbstractMetodoPago:
        """Crear estrategia según el método de pago"""
        config = config or {}

        if metodo == MetodoPago.EFECTIVO:
            return PagoEfectivo()
        elif metodo == MetodoPago.TARJETA:
            terminal_id = config.get('terminal_id', 'TERM-001')
            return PagoTarjeta(terminal_id)
        elif metodo == MetodoPago.TRANSFERENCIA:
            return PagoTransferencia()
        elif metodo == MetodoPago.CHEQUE:
            # Se podría implementar PagoCheque
            raise NotImplementedError("Pago con cheque no implementado")
        else:
            raise ValueError(f"Método de pago no soportado: {metodo}")

# Uso en un use case
class CobrarOrdenUseCase:
    def __init__(self, orden_repo, caja_repo):
        self.orden_repo = orden_repo
        self.caja_repo = caja_repo

    async def execute(self, orden_id: int, metodo: MetodoPago, metadata: dict):
        orden = await self.orden_repo.find_by_id(orden_id)
        if not orden:
            raise ValueError("Orden no encontrada")

        # Crear estrategia según método
        estrategia = PagoStrategyFactory.crear(metodo, metadata)

        # Procesar pago
        resultado = await estrategia.procesar(orden.total, metadata.get('monto_entregado'), metadata)

        if not resultado.exitoso:
            raise ValueError(resultado.mensaje)

        # Actualizar orden
        orden.estado = OrdenEstado.PAGADA
        orden.metodo_pago = metodo
        orden.referencia_pago = resultado.referencia

        await self.orden_repo.save(orden)

        # Registrar en caja si es efectivo
        if metodo == MetodoPago.EFECTIVO:
            await self.caja_repo.registrar_venta_efectivo(orden.total, resultado.cambio)

        return resultado
```

---

## 4. Observer / Event Pattern

Reaccionar a eventos de dominio de forma desacoplada.

### Sistema de eventos de dominio

```python
# app/domain/events/base.py
from abc import ABC, abstractmethod
from datetime import datetime
from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class DomainEvent(ABC):
    """Evento base de dominio"""
    occurred_at: datetime
    aggregate_id: int
    aggregate_type: str
    event_type: str
    data: Dict[str, Any]

@dataclass
class OrdenCreada(DomainEvent):
    """Evento cuando se crea una orden"""
    def __init__(self, orden_id: int, mesa_id: int, tenant_id: int):
        super().__init__(
            occurred_at=datetime.utcnow(),
            aggregate_id=orden_id,
            aggregate_type="Orden",
            event_type="OrdenCreada",
            data={
                "orden_id": orden_id,
                "mesa_id": mesa_id,
                "tenant_id": tenant_id
            }
        )

@dataclass
class OrdenPagada(DomainEvent):
    """Evento cuando se paga una orden"""
    def __init__(self, orden_id: int, monto: float, metodo: str):
        super().__init__(
            occurred_at=datetime.utcnow(),
            aggregate_id=orden_id,
            aggregate_type="Orden",
            event_type="OrdenPagada",
            data={
                "orden_id": orden_id,
                "monto": monto,
                "metodo": metodo
            }
        )

@dataclass
class InventarioBajo(DomainEvent):
    """Evento cuando el inventario está bajo"""
    def __init__(self, producto_id: int, producto_nombre: str, stock_actual: int, stock_minimo: int):
        super().__init__(
            occurred_at=datetime.utcnow(),
            aggregate_id=producto_id,
            aggregate_type="Producto",
            event_type="InventarioBajo",
            data={
                "producto_id": producto_id,
                "producto_nombre": producto_nombre,
                "stock_actual": stock_actual,
                "stock_minimo": stock_minimo
            }
        )
```

### Handlers de eventos

```python
# app/application/handlers/orden_handlers.py
from typing import List
from app.domain.events.base import DomainEvent, OrdenCreada, OrdenPagada, InventarioBajo

class EventHandler(ABC):
    """Handler base para eventos"""

    @abstractmethod
    async def handle(self, event: DomainEvent) -> None:
        """Manejar el evento"""
        pass

    @abstractmethod
    def can_handle(self, event_type: str) -> bool:
        """Determinar si este handler puede manejar el tipo de evento"""
        pass

class NotificarKDSHandler(EventHandler):
    """Notificar al Kitchen Display System cuando se crea una orden"""

    def __init__(self, kds_service):
        self.kds_service = kds_service

    async def handle(self, event: DomainEvent) -> None:
        if isinstance(event, OrdenCreada):
            await self.kds_service.enviar_orden(event.data['orden_id'])

    def can_handle(self, event_type: str) -> bool:
        return event_type == "OrdenCreada"

class DescontarInventarioHandler(EventHandler):
    """Descontar inventario cuando se crea una orden"""

    def __init__(self, inventario_repo):
        self.inventario_repo = inventario_repo

    async def handle(self, event: DomainEvent) -> None:
        if isinstance(event, OrdenCreada):
            await self.inventario_repo.descontar_por_orden(event.data['orden_id'])

    def can_handle(self, event_type: str) -> bool:
        return event_type == "OrdenCreada"

class AlertaInventarioBajoHandler(EventHandler):
    """Enviar alerta cuando el inventario está bajo"""

    def __init__(self, notification_service):
        self.notification_service = notification_service

    async def handle(self, event: DomainEvent) -> None:
        if isinstance(event, InventarioBajo):
            await self.notification_service.enviar_alerta(
                f"Producto {event.data['producto_nombre']} con inventario bajo: "
                f"{event.data['stock_actual']} (mínimo: {event.data['stock_minimo']})"
            )

    def can_handle(self, event_type: str) -> bool:
        return event_type == "InventarioBajo"

class RegistrarVentaCajaHandler(EventHandler):
    """Registrar venta en caja cuando se paga una orden"""

    def __init__(self, caja_repo):
        self.caja_repo = caja_repo

    async def handle(self, event: DomainEvent) -> None:
        if isinstance(event, OrdenPagada):
            await self.caja_repo.registrar_venta(
                monto=event.data['monto'],
                metodo=event.data['metodo']
            )

    def can_handle(self, event_type: str) -> bool:
        return event_type == "OrdenPagada"
```

### Dispatcher de eventos

```python
# app/application/event_dispatcher.py
from typing import List
from app.domain.events.base import DomainEvent
from app.application.handlers.orden_handlers import EventHandler

class EventDispatcher:
    """Dispatcher que enruta eventos a los handlers correspondientes"""

    def __init__(self, handlers: List[EventHandler]):
        self.handlers = handlers

    async def dispatch(self, event: DomainEvent) -> None:
        """Despachar evento a todos los handlers que puedan manejarlo"""
        for handler in self.handlers:
            if handler.can_handle(event.event_type):
                try:
                    await handler.handle(event)
                except Exception as e:
                    # Log error pero continuar con otros handlers
                    print(f"Error en handler {handler.__class__.__name__}: {e}")

# Uso en un use case
class CrearOrdenUseCase:
    def __init__(self, orden_repo, event_dispatcher: EventDispatcher):
        self.orden_repo = orden_repo
        self.event_dispatcher = event_dispatcher

    async def execute(self, data: CrearOrdenInput) -> Orden:
        # Crear orden
        orden = await self.orden_repo.save(Orden(...))

        # Publicar evento
        evento = OrdenCreada(
            orden_id=orden.id,
            mesa_id=orden.mesa_id,
            tenant_id=orden.sucursal_id
        )
        await self.event_dispatcher.dispatch(evento)

        return orden
```

---

## 5. Value Object Pattern

Objetos de valor inmutables con validación incorporada.

### Value Objects con Pydantic

```python
# app/domain/value_objects/common.py
from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

class Email(BaseModel):
    """Value Object para email con validación"""
    value: str = Field(..., min_length=5, max_length=255)

    @field_validator('value')
    @classmethod
    def validar_email(cls, v: str) -> str:
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', v):
            raise ValueError(f'Email inválido: {v}')
        return v.lower()

    def __str__(self) -> str:
        return self.value

class Telefono(BaseModel):
    """Value Object para teléfono mexicano"""
    value: str = Field(..., min_length=10, max_length=15)

    @field_validator('value')
    @classmethod
    def validar_telefono(cls, v: str) -> str:
        # Eliminar espacios y guiones
        telefono = v.replace(' ', '').replace('-', '')

        # Validar longitud
        if len(telefono) < 10:
            raise ValueError(f'Teléfono demasiado corto: {v}')

        # Si no empieza con 52, agregarlo
        if not telefono.startswith('52'):
            telefono = f'52{telefono}'

        return telefono

    @property
    def whatsapp_link(self, mensaje: str = '') -> str:
        """Generar link de WhatsApp"""
        from urllib.parse import quote
        return f"https://wa.me/{self.value}?text={quote(mensaje)}"

    def __str__(self) -> str:
        return self.value

class Dinero(BaseModel):
    """Value Object para cantidades monetarias"""
    value: float = Field(..., ge=0)

    @field_validator('value')
    @classmethod
    def validar_dinero(cls, v: float) -> float:
        # Redondear a 2 decimales
        return round(v, 2)

    @property
    def formato_moneda(self) -> str:
        """Formato de moneda mexicana"""
        return f"${self.value:,.2f} MXN"

    def __add__(self, other: 'Dinero') -> 'Dinero':
        return Dinero(value=self.value + other.value)

    def __sub__(self, other: 'Dinero') -> 'Dinero':
        return Dinero(value=max(0, self.value - other.value))

    def __mul__(self, factor: float) -> 'Dinero':
        return Dinero(value=self.value * factor)

    def __str__(self) -> str:
        return self.formato_moneda

class RFC(BaseModel):
    """Value Object para RFC mexicano"""
    value: str = Field(..., min_length=12, max_length=13)

    @field_validator('value')
    @classmethod
    def validar_rfc(cls, v: str) -> str:
        rfc = v.upper().strip()

        # Validar formato básico
        if len(rfc) not in [12, 13]:
            raise ValueError(f'RFC debe tener 12 (moral) o 13 (física) caracteres: {v}')

        # Validar que sean letras y números
        if not re.match(r'^[A-ZÑ&]{3,4}[0-9]{6}[A-Z0-9]{3}$', rfc):
            raise ValueError(f'RFC inválido: {v}')

        return rfc

    @property
    def es_persona_fisica(self) -> bool:
        """Determinar si es persona física (13 caracteres)"""
        return len(self.value) == 13

    @property
    def es_persona_moral(self) -> bool:
        """Determinar si es persona moral (12 caracteres)"""
        return len(self.value) == 12

    def __str__(self) -> str:
        return self.value

class CURP(BaseModel):
    """Value Object para CURP mexicano"""
    value: str = Field(..., min_length=18, max_length=18)

    @field_validator('value')
    @classmethod
    def validar_curp(cls, v: str) -> str:
        curp = v.upper().strip()

        # Validar longitud
        if len(curp) != 18:
            raise ValueError(f'CURP debe tener 18 caracteres: {v}')

        # Validar formato básico
        if not re.match(r'^[A-Z]{4}[0-9]{6}[A-Z]{6}[0-9A-Z]{2}$', curp):
            raise ValueError(f'CURP inválido: {v}')

        return curp

    def __str__(self) -> str:
        return self.value
```

### Uso de Value Objects en entidades

```python
# app/domain/entities/usuario.py
from dataclasses import dataclass
from datetime import datetime
from app.domain.value_objects.common import Email, Telefono, RFC

@dataclass
class Usuario:
    id: Optional[int]
    email: Email  # No str, sino Value Object
    nombre: str
    telefono: Telefono  # Value Object con validación
    rfc: Optional[RFC]  # Value Object opcional
    rol: str
    activo: bool = True
    created_at: Optional[datetime] = None

    # El constructor ya valida los VOs automáticamente
    # No necesitas validar en cada método
```

---

## 6. Unit of Work Pattern

Manejar transacciones atómicas entre múltiples repositorios.

### Unit of Work con SQLAlchemy

```python
# app/infrastructure/persistence/unit_of_work.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.persistence.repositories import (
    SQLAlchemyOrdenRepository,
    SQLAlchemyInventarioRepository,
    SQLAlchemyCajaRepository,
    SQLAlchemyUsuarioRepository
)

class UnitOfWork:
    """Unit of Work que agrupa múltiples repositorios en una transacción"""

    def __init__(self, session_factory, sucursal_id: Optional[int] = None):
        self.session_factory = session_factory
        self.sucursal_id = sucursal_id

    async def __aenter__(self):
        """Entrar al contexto de transacción"""
        self.session: AsyncSession = self.session_factory()

        # Inicializar repositorios con la misma sesión
        self.ordenes = SQLAlchemyOrdenRepository(self.session, self.sucursal_id)
        self.inventario = SQLAlchemyInventarioRepository(self.session, self.sucursal_id)
        self.caja = SQLAlchemyCajaRepository(self.session, self.sucursal_id)
        self.usuarios = SQLAlchemyUsuarioRepository(self.session, self.sucursal_id)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Salir del contexto y manejar commit/rollback"""
        try:
            if exc_type is None:
                await self.session.commit()
            else:
                await self.session.rollback()
        finally:
            await self.session.close()

    async def commit(self):
        """Commit explícito (opcional, el contexto ya lo hace)"""
        await self.session.commit()

    async def rollback(self):
        """Rollback explícito"""
        await self.session.rollback()
```

### Uso en Use Case

```python
# app/application/use_cases/cobrar_orden.py
from app.infrastructure.persistence.unit_of_work import UnitOfWork

class CobrarOrdenUseCase:
    def __init__(self, uow_factory, event_dispatcher):
        self.uow_factory = uow_factory
        self.event_dispatcher = event_dispatcher

    async def execute(self, orden_id: int, metodo_pago: str, monto_entregado: float = None):
        """Cobrar orden de forma atómica: actualizar orden + descontar inventario + registrar caja"""
        async with self.uow_factory() as uow:
            # 1. Obtener orden
            orden = await uow.ordenes.find_by_id(orden_id)
            if not orden:
                raise ValueError("Orden no encontrada")

            # 2. Procesar pago
            resultado = await self._procesar_pago(orden, metodo_pago, monto_entregado)

            # 3. Actualizar estado de orden
            orden.estado = OrdenEstado.PAGADA
            orden.metodo_pago = metodo_pago
            orden.referencia_pago = resultado.referencia
            await uow.ordenes.save(orden)

            # 4. Descontar inventario
            for item in orden.items:
                await uow.inventario.descontar(
                    producto_id=item.producto_id,
                    cantidad=item.cantidad
                )

            # 5. Registrar en caja
            await uow.caja.registrar_venta(
                monto=orden.total,
                metodo=metodo_pago,
                cambio=resultado.cambio
            )

            # 6. Publicar evento (fuera de la transacción)
            evento = OrdenPagada(
                orden_id=orden.id,
                monto=orden.total,
                metodo=metodo_pago
            )

            # El commit del contexto garantiza que todo se guarde atómicamente
            # o nada se guarde si hay error

        # Publicar evento después del commit
        await self.event_dispatcher.dispatch(evento)

        return resultado
```

---

## 7. Middleware de Autenticación

Middleware FastAPI para validar JWT y obtener usuario actual.

### get_current_user dependency

```python
# app/adapters/http/middleware/auth.py
from fastapi import Depends, HTTPException, status, Cookie, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

from app.core.config import settings
from app.domain.entities.usuario import Usuario
from app.infrastructure.persistence.repositories import SQLAlchemyUsuarioRepository

security = HTTPBearer()

async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    access_token: Optional[str] = Cookie(None),
    db: AsyncSession = Depends(get_db)
) -> Usuario:
    """
    Obtener usuario actual desde JWT token.
    Soporta token en Authorization header (Bearer) o cookie (para SSR).
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No autenticado",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Determinar de dónde obtener el token
    token = None
    if credentials:
        token = credentials.credentials
    elif access_token:
        token = access_token

    if not token:
        raise credentials_exception

    try:
        # Decodificar JWT
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception

        # Verificar expiración
        exp = payload.get("exp")
        if exp and datetime.utcnow() > datetime.fromtimestamp(exp):
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    # Obtener usuario desde DB
    usuario_repo = SQLAlchemyUsuarioRepository(db)
    usuario = await usuario_repo.find_by_id(user_id)

    if usuario is None:
        raise credentials_exception

    if not usuario.activo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo"
        )

    return usuario
```

### Decorator de roles

```python
# app/adapters/http/middleware/roles.py
from functools import wraps
from fastapi import HTTPException, status

def require_role(*roles_permitidos: str):
    """
    Decorador para restringir acceso por roles.

    Uso:
    @router.get("/admin")
    @require_role("admin", "gerente")
    async def admin_endpoint(usuario: Usuario = Depends(get_current_user)):
        ...
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Buscar el usuario en los argumentos
            usuario = None
            for arg in args:
                if isinstance(arg, Usuario):
                    usuario = arg
                    break

            if not usuario:
                for key, value in kwargs.items():
                    if isinstance(value, Usuario):
                        usuario = value
                        break

            if not usuario:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="No autenticado"
                )

            if usuario.rol not in roles_permitidos:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Se requiere uno de estos roles: {', '.join(roles_permitidos)}"
                )

            return await func(*args, **kwargs)
        return wrapper
    return decorator

# Alternativa: usar dependency de FastAPI
async def require_role_dependency(*roles_permitidos: str, usuario: Usuario = Depends(get_current_user)):
    """Dependency de FastAPI para requerir roles"""
    if usuario.rol not in roles_permitidos:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Se requiere uno de estos roles: {', '.join(roles_permitidos)}"
        )
    return usuario

# Uso en endpoints
@router.get("/admin/usuarios")
async def listar_usuarios(
    admin: Usuario = Depends(require_role_dependency("admin", "gerente"))
):
    # Solo admins y gerentes pueden acceder
    ...
```

---

## 8. Service Layer Pattern

Separar lógica de negocio de los controllers.

### Servicio de autenticación

```python
# app/application/services/auth_service.py
from datetime import datetime, timedelta
from jose import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from app.core.config import settings
from app.domain.entities.usuario import Usuario
from app.domain.value_objects.common import Email
from app.infrastructure.persistence.repositories import SQLAlchemyUsuarioRepository

ph = PasswordHasher()

class AuthService:
    """Servicio de autenticación y autorización"""

    def __init__(self, usuario_repo: SQLAlchemyUsuarioRepository):
        self.usuario_repo = usuario_repo

    async def registrar(
        self,
        email: str,
        password: str,
        nombre: str,
        rol: str = "usuario"
    ) -> Usuario:
        """Registrar nuevo usuario"""
        # Validar email único
        email_vo = Email(value=email)
        existente = await self.usuario_repo.find_by_email(email_vo.value)

        if existente:
            raise ValueError("Email ya registrado")

        # Hash password con Argon2id
        password_hash = ph.hash(password)

        # Crear usuario
        usuario = Usuario(
            id=None,
            email=email_vo,
            nombre=nombre,
            rol=rol,
            password_hash=password_hash,
            activo=True,
            created_at=datetime.utcnow()
        )

        return await self.usuario_repo.save(usuario)

    async def login(self, email: str, password: str) -> dict:
        """Iniciar sesión y retornar tokens"""
        # Buscar usuario
        usuario = await self.usuario_repo.find_by_email(email)

        if not usuario:
            raise ValueError("Credenciales inválidas")

        if not usuario.activo:
            raise ValueError("Usuario inactivo")

        # Verificar password
        try:
            ph.verify(usuario.password_hash, password)

            # Rehash si necesario (mejora seguridad gradualmente)
            if ph.check_needs_rehash(usuario.password_hash):
                usuario.password_hash = ph.hash(password)
                await self.usuario_repo.save(usuario)

        except VerifyMismatchError:
            raise ValueError("Credenciales inválidas")

        # Generar tokens
        access_token = self._create_access_token(usuario)
        refresh_token = self._create_refresh_token(usuario)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "usuario": {
                "id": usuario.id,
                "email": usuario.email.value,
                "nombre": usuario.nombre,
                "rol": usuario.rol
            }
        }

    async def refresh_token(self, refresh_token: str) -> dict:
        """Refrescar access token usando refresh token"""
        try:
            payload = jwt.decode(
                refresh_token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )

            user_id = payload.get("sub")
            token_type = payload.get("type")

            if token_type != "refresh":
                raise ValueError("Token inválido")

            usuario = await self.usuario_repo.find_by_id(user_id)

            if not usuario or not usuario.activo:
                raise ValueError("Token inválido")

            access_token = self._create_access_token(usuario)

            return {
                "access_token": access_token,
                "token_type": "bearer"
            }

        except JWTError:
            raise ValueError("Token inválido")

    def _create_access_token(self, usuario: Usuario) -> str:
        """Crear JWT access token"""
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        expires = datetime.utcnow() + expires_delta

        to_encode = {
            "sub": usuario.id,
            "email": usuario.email.value,
            "rol": usuario.rol,
            "exp": expires,
            "type": "access"
        }

        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    def _create_refresh_token(self, usuario: Usuario) -> str:
        """Crear JWT refresh token (más duradero)"""
        expires_delta = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        expires = datetime.utcnow() + expires_delta

        to_encode = {
            "sub": usuario.id,
            "exp": expires,
            "type": "refresh"
        }

        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
```

---

## 9. Dependency Injection Manual

Inyección de dependencias sin framework (FastAPI Depends).

### Container de dependencias

```python
# app/core/container.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from typing import Optional

from app.infrastructure.persistence.repositories import (
    SQLAlchemyOrdenRepository,
    SQLAlchemyInventarioRepository,
    SQLAlchemyCajaRepository,
    SQLAlchemyUsuarioRepository
)
from app.application.services.auth_service import AuthService
from app.application.use_cases import (
    CrearOrdenUseCase,
    CobrarOrdenUseCase,
    ListarOrdenesUseCase
)
from app.application.event_dispatcher import EventDispatcher
from app.application.handlers import (
    NotificarKDSHandler,
    DescontarInventarioHandler,
    AlertaInventarioBajoHandler,
    RegistrarVentaCajaHandler
)

class Container:
    """Container manual de inyección de dependencias"""

    def __init__(self):
        self._engine = None
        self._session_factory = None
        self._initialized = False

    def initialize(self, database_url: str):
        """Inicializar container con configuración"""
        self._engine = create_async_engine(
            database_url,
            echo=False,
            future=True
        )

        self._session_factory = async_sessionmaker(
            self._engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

        self._initialized = True

    @property
    def session_factory(self):
        """Factory para crear sesiones de DB"""
        if not self._initialized:
            raise RuntimeError("Container no inicializado")
        return self._session_factory

    # Repositorios
    def orden_repository(self, session: AsyncSession, sucursal_id: Optional[int] = None):
        return SQLAlchemyOrdenRepository(session, sucursal_id)

    def inventario_repository(self, session: AsyncSession, sucursal_id: Optional[int] = None):
        return SQLAlchemyInventarioRepository(session, sucursal_id)

    def caja_repository(self, session: AsyncSession, sucursal_id: Optional[int] = None):
        return SQLAlchemyCajaRepository(session, sucursal_id)

    def usuario_repository(self, session: AsyncSession, sucursal_id: Optional[int] = None):
        return SQLAlchemyUsuarioRepository(session, sucursal_id)

    # Servicios
    def auth_service(self, session: AsyncSession):
        usuario_repo = self.usuario_repository(session)
        return AuthService(usuario_repo)

    # Event dispatcher
    def event_dispatcher(self, session: AsyncSession):
        inventario_repo = self.inventario_repository(session)
        caja_repo = self.caja_repository(session)

        handlers = [
            NotificarKDSHandler(kds_service=None),  # Inyectar servicio real
            DescontarInventarioHandler(inventario_repo),
            AlertaInventarioBajoHandler(notification_service=None),
            RegistrarVentaCajaHandler(caja_repo)
        ]

        return EventDispatcher(handlers)

    # Use Cases
    def crear_orden_use_case(self, session: AsyncSession, sucursal_id: Optional[int] = None):
        orden_repo = self.orden_repository(session, sucursal_id)
        event_dispatcher = self.event_dispatcher(session)
        return CrearOrdenUseCase(orden_repo, event_dispatcher)

    def cobrar_orden_use_case(self, session: AsyncSession, sucursal_id: Optional[int] = None):
        uow = UnitOfWork(self.session_factory, sucursal_id)
        event_dispatcher = self.event_dispatcher(session)
        return CobrarOrdenUseCase(uow, event_dispatcher)

    def listar_ordenes_use_case(self, session: AsyncSession, sucursal_id: Optional[int] = None):
        orden_repo = self.orden_repository(session, sucursal_id)
        return ListarOrdenesUseCase(orden_repo)

# Instancia global del container
container = Container()
```

### Uso en FastAPI

```python
# app/adapters/http/dependencies.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.container import container

async def get_db() -> AsyncSession:
    """Dependency para obtener sesión de DB"""
    async with container.session_factory() as session:
        try:
            yield session
        finally:
            await session.close()

async def get_auth_service(
    db: AsyncSession = Depends(get_db)
) -> AuthService:
    """Dependency para obtener AuthService"""
    return container.auth_service(db)

async def get_crear_orden_use_case(
    db: AsyncSession = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
) -> CrearOrdenUseCase:
    """Dependency para obtener CrearOrdenUseCase"""
    sucursal_id = current_user.sucursal_id if current_user.rol != "admin" else None
    return container.crear_orden_use_case(db, sucursal_id)

# Uso en routers
@router.post("/ordenes")
async def crear_orden(
    data: CrearOrdenInput,
    uc: CrearOrdenUseCase = Depends(get_crear_orden_use_case)
):
    return await uc.execute(data)
```

---

## 10. Configuration Pattern

Configuración centralizada con Pydantic Settings.

### Configuración con Pydantic BaseSettings

```python
# app/core/config.py
from pydantic import BaseSettings, Field
from typing import Optional
from functools import lru_cache

class Settings(BaseSettings):
    """Configuración de la aplicación con Pydantic"""

    # App
    APP_NAME: str = "FastAPI App"
    APP_VERSION: str = "2.0.0"
    DEBUG: bool = False

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Database
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    DATABASE_POOL_SIZE: int = 5
    DATABASE_MAX_OVERFLOW: int = 10

    # Security
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8000"]

    # Email
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: int = 587
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAIL_FROM: Optional[str] = None

    # Storage
    UPLOAD_DIR: str = "uploads"
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB

    # Tenant
    DEFAULT_SUCURSAL_ID: Optional[int] = None

    # Features
    ENABLE_REGISTRATION: bool = True
    REQUIRE_EMAIL_VERIFICATION: bool = False

    # External Services
    KDS_WEBHOOK_URL: Optional[str] = None
    WHATSAPP_API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    """Obtener instancia cacheada de settings"""
    return Settings()

settings = get_settings()
```

### .env.example

```bash
# App
APP_NAME="Mi App FastAPI"
DEBUG=true

# Database
DATABASE_URL=sqlite+aiosqlite:///./app.db
# Para PostgreSQL:
# DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname

# Security
SECRET_KEY=your-secret-key-change-this-in-production

# Email (opcional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
EMAIL_FROM=noreply@yourapp.com

# External Services (opcional)
KDS_WEBHOOK_URL=https://kds.example.com/webhook
WHATSAPP_API_KEY=your-api-key
```

---

## Conclusión

Estos patrones proporcionan una base sólida para aplicaciones FastAPI escalables y mantenibles. No es necesario aplicarlos todos en cada proyecto, pero entenderlos permite elegir el correcto para cada situación.

**Patrones recomendados para empezar:**
1. Repository Pattern (siempre)
2. Unit of Work (cuando hay múltiples operaciones atómicas)
3. Value Objects (para datos con validación)
4. Service Layer (para lógica de negocio compleja)
5. Configuration Pattern (siempre)

**Patrones opcionales según necesidad:**
- Factory Pattern (creación de objetos complejos)
- Strategy Pattern (algoritmos intercambiables)
- Observer/Event Pattern (efectos secundarios desacoplados)
- Middleware/Decorator de roles (autorización)
- Dependency Injection Manual (cuando Depends de FastAPI no es suficiente)
