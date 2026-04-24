### 1. Introducción a PostgreSQL

**¿Qué es PostgreSQL?**  
PostgreSQL es un sistema de gestión de bases de datos relacional (RDBMS) de código abierto, altamente escalable y compatible con los estándares SQL. Es conocido por su robustez, extensibilidad y soporte para consultas complejas, índices avanzados y transacciones seguras.

**Ventajas de PostgreSQL**:

- **Open Source**: PostgreSQL es gratuito y cuenta con una comunidad activa.
- **Soporte de ACID**: Cumple con las propiedades de Atomicidad, Consistencia, Aislamiento y Durabilidad, esenciales para transacciones seguras.
- **Escalabilidad y Extensibilidad**: Soporta grandes volúmenes de datos y extensiones avanzadas (como PostGIS para datos geoespaciales).

**Conceptos clave**:

- **Tablas**: Almacenan datos en filas y columnas.
- **Esquemas**: Permiten organizar tablas dentro de una base de datos.
- **Relaciones**: Conexiones lógicas entre tablas usando claves primarias y foráneas.

---

### 2. Instalación de PostgreSQL

**Instalación en Windows**:

1. Descarga el instalador desde la [página oficial de PostgreSQL](https://www.postgresql.org/download/).
2. Sigue las instrucciones del instalador y toma nota del usuario y la contraseña.
3. Durante la instalación, elige componentes opcionales como **pgAdmin** para una interfaz gráfica.

**Instalación en macOS**:

1. Usa Homebrew para instalar PostgreSQL:
    
    bash
    
    Copiar código
    
    `brew install postgresql`
    
2. Inicia PostgreSQL:
    
    bash
    
    Copiar código
    
    `brew services start postgresql`
    

**Instalación en Linux (Debian/Ubuntu)**:

1. Actualiza los paquetes:
    
    bash
    
    Copiar código
    
    `sudo apt update`
    
2. Instala PostgreSQL:
    
    bash
    
    Copiar código
    
    `sudo apt install postgresql postgresql-contrib`
    
3. Inicia el servicio de PostgreSQL:
    
    bash
    
    Copiar código
    
    `sudo systemctl start postgresql`
    

**Verificación de la instalación**: Conéctate a PostgreSQL usando el comando `psql`:

bash

Copiar código

`sudo -u postgres psql`

---

### 3. Conexión y Configuración Inicial

**Conexión usando `psql`**: El cliente `psql` permite ejecutar consultas SQL en la línea de comandos.

bash

Copiar código

`sudo -u postgres psql`

**Configuración de usuarios y roles**:

1. **Crear un usuario**:
    
    sql
    
    Copiar código
    
    `CREATE USER mi_usuario WITH PASSWORD 'mi_contraseña';`
    
2. **Crear una base de datos**:
    
    sql
    
    Copiar código
    
    `CREATE DATABASE mi_base_de_datos;`
    
3. **Asignar permisos al usuario**:
    
    sql
    
    Copiar código
    
    `GRANT ALL PRIVILEGES ON DATABASE mi_base_de_datos TO mi_usuario;`
    

---

### 4. Estructura Básica de PostgreSQL

**Tablas y tipos de datos**:

1. PostgreSQL soporta tipos de datos básicos (`INTEGER`, `VARCHAR`, `DATE`) y avanzados (`JSON`, `ARRAY`).
2. **Creación de una tabla**:
    
    sql
    
    Copiar código
    
    `CREATE TABLE empleados (     id SERIAL PRIMARY KEY,     nombre VARCHAR(50),     puesto VARCHAR(50),     salario NUMERIC(10, 2),     fecha_contratacion DATE );`
    

**Relaciones**:

- **Llaves primarias**: Un identificador único para cada registro en una tabla.
- **Llaves foráneas**: Permiten conectar datos entre tablas.

---

### 5. Consultas SQL Básicas en PostgreSQL

**Insertar datos**:

sql

Copiar código

`INSERT INTO empleados (nombre, puesto, salario, fecha_contratacion) VALUES ('Juan Perez', 'Gerente', 50000.00, '2022-01-15');`

**Consultar datos**:

sql

Copiar código

`SELECT * FROM empleados;`

**Actualizar datos**:

sql

Copiar código

`UPDATE empleados SET salario = 55000.00 WHERE nombre = 'Juan Perez';`

**Eliminar datos**:

sql

Copiar código

`DELETE FROM empleados WHERE nombre = 'Juan Perez';`

---

### 6. Consultas SQL Avanzadas en PostgreSQL

**Joins**:

1. **INNER JOIN**:
    
    sql
    
    Copiar código
    
    `SELECT empleados.nombre, departamentos.nombre AS departamento FROM empleados INNER JOIN departamentos ON empleados.departamento_id = departamentos.id;`
    
2. **LEFT JOIN**:
    
    sql
    
    Copiar código
    
    `SELECT empleados.nombre, departamentos.nombre AS departamento FROM empleados LEFT JOIN departamentos ON empleados.departamento_id = departamentos.id;`
    

**Funciones de agregación**:

sql

Copiar código

`SELECT COUNT(*), AVG(salario), SUM(salario) FROM empleados;`

**Subconsultas**:

sql

Copiar código

`SELECT nombre, salario FROM empleados WHERE salario > (SELECT AVG(salario) FROM empleados);`

**Vistas**:

sql

Copiar código

`CREATE VIEW vista_empleados_salario AS SELECT nombre, salario FROM empleados WHERE salario > 50000;`

---

### 7. Índices y Optimización de Consultas

**Crear un índice**:

sql

Copiar código

`CREATE INDEX idx_empleados_nombre ON empleados(nombre);`

**Analizar rendimiento con `EXPLAIN`**:

sql

Copiar código

`EXPLAIN SELECT * FROM empleados WHERE nombre = 'Juan Perez';`

> **Nota**: Los índices mejoran el rendimiento de consultas en campos de búsqueda frecuente, aunque aumentan el tiempo de inserción y actualización.

---

### 8. Administración y Seguridad de la Base de Datos

**Creación y gestión de roles**:

1. **Crear un rol**:
    
    sql
    
    Copiar código
    
    `CREATE ROLE analista WITH LOGIN PASSWORD 'contraseña';`
    
2. **Asignar permisos**:
    
    sql
    
    Copiar código
    
    `GRANT SELECT ON empleados TO analista;`
    

**Configuración de acceso y autenticación**: El archivo `pg_hba.conf` (ubicado generalmente en `/etc/postgresql/`) controla la autenticación y permite limitar el acceso a ciertos usuarios o direcciones IP.

---

### 9. Backups y Recuperación de Datos

**Realizar una copia de seguridad**:

bash

Copiar código

`pg_dump mi_base_de_datos > backup.sql`

**Restaurar desde una copia de seguridad**:

bash

Copiar código

`psql -U mi_usuario -d mi_base_de_datos -f backup.sql`

> **Consejo**: Realizar copias de seguridad regulares es esencial en entornos de producción.

---

### 10. Extensiones y Funcionalidades Avanzadas de PostgreSQL

**Instalación de una extensión**: PostgreSQL soporta extensiones que amplían sus capacidades, como **PostGIS** para datos geoespaciales.

sql

Copiar código

`CREATE EXTENSION IF NOT EXISTS postgis;`

**Tablas particionadas**: PostgreSQL permite dividir grandes tablas en subtablas para mejorar el rendimiento y la gestión de datos.

sql

Copiar código

`CREATE TABLE ventas (     id SERIAL,     fecha DATE,     total NUMERIC ) PARTITION BY RANGE (fecha);`

---

### Conclusión y Práctica

**Ejercicio práctico**:

1. Crea una base de datos y añade una tabla de empleados.
2. Inserta algunos registros y realiza consultas de selección.
3. Crea una vista y realiza un JOIN con otra tabla.
4. Genera un índice y prueba el rendimiento de las consultas.

**Autoevaluación**: Revisa si puedes realizar consultas básicas y avanzadas sin dificultad, además de configurar la seguridad y administración básica en PostgreSQL.

### Instalación de PostgreSQL desde Docker

Docker es una herramienta útil para instalar y ejecutar PostgreSQL en un contenedor, evitando instalar directamente en el sistema y facilitando su administración y despliegue.

#### 1. Instalación de Docker

Si aún no tienes Docker instalado, puedes seguir las instrucciones en la documentación oficial de Docker.

#### 2. Descargar e Iniciar un Contenedor de PostgreSQL

1. **Descargar la imagen de PostgreSQL**:
    
    bash
    
    Copiar código
    
    `docker pull postgres`
    
    Esto descarga la última versión oficial de PostgreSQL.
    
2. **Ejecutar el contenedor de PostgreSQL**:
    
    bash
    
    Copiar código
    
    `docker run --name mi_postgres -e POSTGRES_PASSWORD=mi_contraseña -p 5432:5432 -d postgres`
    
    - `--name mi_postgres`: Asigna el nombre `mi_postgres` al contenedor.
    - `-e POSTGRES_PASSWORD=mi_contraseña`: Configura la contraseña para el usuario `postgres`.
    - `-p 5432:5432`: Abre el puerto 5432, necesario para conectarse a PostgreSQL.
    - `-d`: Ejecuta el contenedor en modo “desprendido” (background).
3. **Verificar que el contenedor esté en ejecución**:
    
    bash
    
    Copiar código
    
    `docker ps`
    
    Esto mostrará el contenedor `mi_postgres` en ejecución, con PostgreSQL listo para recibir conexiones en el puerto `5432`.
    

#### 3. Conexión a PostgreSQL desde el Contenedor

Una vez que PostgreSQL está en ejecución en Docker, puedes conectarte usando `psql` o herramientas como pgAdmin:

- **Conexión usando `psql`**:
    
    bash
    
    Copiar código
    
    `docker exec -it mi_postgres psql -U postgres`
    
    Esto te permite acceder a PostgreSQL como el usuario `postgres` desde dentro del contenedor.

#### 4. Persistencia de Datos con Docker Volumes

Para evitar que los datos se eliminen al detener el contenedor, puedes montar un volumen local:

bash

Copiar código

`docker run --name mi_postgres -e POSTGRES_PASSWORD=mi_contraseña -p 5432:5432 -v /ruta/local:/var/lib/postgresql/data -d postgres`

- `-v /ruta/local:/var/lib/postgresql/data`: Monta una carpeta local como volumen para almacenar los datos.

---

### Ventajas y Desventajas de PostgreSQL frente a MongoDB

PostgreSQL y MongoDB son sistemas de bases de datos que sirven diferentes propósitos, y elegir uno sobre el otro dependerá de tus necesidades.

#### Ventajas de PostgreSQL

1. **Soporte Relacional**: PostgreSQL es una base de datos relacional (RDBMS) que permite la organización de datos en tablas relacionadas mediante llaves foráneas.
2. **Cumple con ACID**: Esto garantiza transacciones seguras y consistentes.
3. **Lenguaje SQL Completo**: PostgreSQL es compatible con SQL, lo que facilita consultas complejas.
4. **Extensibilidad**: Ofrece funciones avanzadas como JSON, arrays y soporte para geolocalización (con extensiones como PostGIS).

#### Desventajas de PostgreSQL

1. **Escalabilidad Horizontal Limitada**: PostgreSQL no escala tan fácilmente como MongoDB en una arquitectura de clúster distribuido.
2. **Menor Flexibilidad en la Estructura de Datos**: Los datos deben seguir un esquema más rígido en comparación con el almacenamiento flexible de MongoDB.

#### Ventajas de MongoDB

1. **Base de Datos NoSQL**: Almacena datos en documentos JSON, lo que permite una estructura flexible.
2. **Alta Escalabilidad**: MongoDB escala horizontalmente de manera efectiva, ideal para aplicaciones distribuidas.
3. **Desarrollo Rápido**: Su esquema flexible facilita cambios en el diseño de la base de datos sin una estructura rígida.

#### Desventajas de MongoDB

1. **Inconsistencia Eventual**: Al no seguir las normas ACID al mismo nivel que PostgreSQL, puede haber inconsistencias en algunas transacciones.
2. **Limitado para Consultas Complejas**: No ofrece un lenguaje de consulta SQL completo, y las consultas complejas pueden ser menos eficientes.

---

### Ejemplos de Llaves Foráneas en PostgreSQL

Las **llaves foráneas** permiten crear relaciones entre tablas. En PostgreSQL, se definen como referencias entre una columna de una tabla y la columna primaria de otra tabla.

#### Ejemplo: Relaciones entre Tablas de Empleados y Departamentos

Supongamos que queremos una base de datos donde cada **empleado** pertenezca a un **departamento**. Crearemos dos tablas: `departamentos` y `empleados`, donde `empleados` tendrá una llave foránea que se refiere a `departamentos`.

1. **Crear la Tabla `departamentos`**:
    
    sql
    
    Copiar código
    
    `CREATE TABLE departamentos (     id SERIAL PRIMARY KEY,  -- ID único para cada departamento     nombre VARCHAR(100) NOT NULL  -- Nombre del departamento );`
    
2. **Crear la Tabla `empleados` con Llave Foránea**:
    
    sql
    
    Copiar código
    
    `CREATE TABLE empleados (     id SERIAL PRIMARY KEY,  -- ID único para cada empleado     nombre VARCHAR(100) NOT NULL,  -- Nombre del empleado     puesto VARCHAR(50),  -- Puesto del empleado     departamento_id INTEGER,  -- Llave foránea que conecta con la tabla departamentos     FOREIGN KEY (departamento_id) REFERENCES departamentos (id)  -- Definición de la llave foránea );`
    
    En este ejemplo, `departamento_id` en la tabla `empleados` es una llave foránea que referencia `id` en `departamentos`. Esto asegura que cada empleado esté asociado a un departamento válido.
    

#### Insertar Datos para Ver la Relación

1. **Agregar Departamentos**:
    
    sql
    
    Copiar código
    
    `INSERT INTO departamentos (nombre) VALUES ('Recursos Humanos'), ('Marketing');`
    
2. **Agregar Empleados Asociados a Departamentos**:
    
    sql
    
    Copiar código
    
    `INSERT INTO empleados (nombre, puesto, departamento_id) VALUES ('Ana Gómez', 'Gerente', 1), ('Carlos López', 'Analista', 2);`
    
3. **Consulta con `JOIN` para Ver los Datos Relacionados**:
    
    sql
    
    Copiar código
    
    `SELECT empleados.nombre AS Empleado, empleados.puesto AS Puesto, departamentos.nombre AS Departamento FROM empleados INNER JOIN departamentos ON empleados.departamento_id = departamentos.id;`
    

Este `JOIN` une ambas tablas y muestra cada empleado con su respectivo departamento.

---

### Práctica y Autoevaluación

1. **Ejercicio en Docker**:
    
    - Lanza una instancia de PostgreSQL en Docker.
    - Conéctate a la base de datos y crea las tablas `departamentos` y `empleados`.
    - Inserta datos de prueba y consulta las relaciones.
2. **Reflexiona sobre Ventajas y Desventajas**:
    
    - Si tienes alguna aplicación en mente, analiza si PostgreSQL o MongoDB se adapta mejor a sus necesidades en términos de consistencia, escalabilidad y flexibilidad de esquema.
3. **Consulta con Llaves Foráneas**:
    
    - Crea tus propias tablas relacionadas y realiza `JOINs` para practicar las relaciones.





En PostgreSQL, los **dominios** son un tipo de datos definidos por el usuario que permiten crear un tipo de datos personalizado con reglas adicionales. Un dominio es una extensión de un tipo de datos básico (como `INTEGER`, `VARCHAR`, `DATE`, etc.) a la que se le pueden agregar restricciones como `CHECK`, `NOT NULL`, entre otras.

### ¿Para qué sirven los dominios?

Los dominios son útiles para los siguientes casos:

1. **Reutilización de tipos de datos**: Si tienes un conjunto de columnas en varias tablas que comparten las mismas restricciones y tipo de dato, puedes definir un dominio y usarlo en todas esas columnas, evitando redundancia y facilitando el mantenimiento.
    
2. **Restricciones comunes**: Puedes aplicar restricciones comunes (como rangos de valores o valores permitidos) de manera centralizada. Esto asegura que todas las tablas que usen el dominio cumplan con las mismas reglas.
    
3. **Simplificación del esquema**: Ayuda a que el esquema sea más limpio y más fácil de entender, ya que se pueden aplicar reglas de validación comunes a través de los dominios en lugar de hacerlo en cada columna individual.
    

### Ejemplo de dominio en PostgreSQL

Supongamos que quieres crear un dominio para representar un código de país, donde el valor es siempre una cadena de caracteres de exactamente 3 letras, y solo se permiten códigos alfabéticos.

1. Primero, defines el dominio: