# Tutorial: Sistema de Registro de Alumnos en Go

## Estructura del Proyecto

```
registro_alumnos/
├── main.go                 # Punto de entrada de la aplicación
├── config/                 # Configuraciones
│   └── database.go        # Configuración de la base de datos
├── models/                 # Modelos de datos
│   └── models.go          # Definición de estructuras y operaciones de BD
├── controllers/           # Controladores
│   └── controllers.go     # Lógica de manejo de peticiones
├── routes/                # Rutas
│   └── routes.go         # Configuración del router
└── templates/            # Plantillas HTML
    ├── layout.html       # Plantilla base
    ├── index.html        # Página principal
    ├── form.html         # Formulario de registro
    ├── reporte_grupo.html # Reporte por grupo
    └── reporte_dia.html   # Reporte por día
```

## 1. Main.go - Punto de Entrada

```go
package main

import (
    "log"
    "registro_alumnos/config"
    "registro_alumnos/routes"
)

func main() {
    // Inicializar base de datos
    db, err := config.InitDB()
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    // Inicializar router
    r := routes.SetupRouter(db)

    // Iniciar servidor
    r.Run(":8080")
}
```

**Explicación línea por línea:**
1. `package main`: Declara que este es el paquete principal del programa
2. Las importaciones incluyen:
   - `log`: Para registro de errores
   - `config`: Nuestro paquete de configuración
   - `routes`: Nuestro paquete de rutas

3. `func main()`: Punto de entrada principal del programa
4. `db, err := config.InitDB()`: Inicializa la conexión a la base de datos
5. `defer db.Close()`: Asegura que la conexión se cierre cuando termine el programa
6. `r := routes.SetupRouter(db)`: Configura el router con la conexión a la BD
7. `r.Run(":8080")`: Inicia el servidor en el puerto 8080

## 2. Config/database.go - Configuración de Base de Datos

```go
package config

import (
    "database/sql"
    _ "github.com/mattn/go-sqlite3"
)
```

**Explicación de la configuración de base de datos:**
1. Importa el paquete SQL estándar y el driver de SQLite3
2. La función `InitDB()` realiza:
   - Crea una conexión a SQLite3
   - Crea las tablas si no existen
   - Inserta grupos predeterminados
   - Retorna la conexión a la BD

### Estructura de las tablas:
```sql
CREATE TABLE grupos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT UNIQUE NOT NULL
);

CREATE TABLE registros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mes TEXT NOT NULL,
    fecha DATE NOT NULL,
    alumno TEXT NOT NULL,
    grupo_id INTEGER NOT NULL,
    matricula TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (grupo_id) REFERENCES grupos(id)
);
```

## 3. Models/models.go - Modelos de Datos

### Estructuras de Datos
```go
type Grupo struct {
    ID     int    `json:"id"`
    Numero string `json:"numero"`
}

type Registro struct {
    ID          int       `json:"id"`
    Mes         string    `json:"mes"`
    Fecha       string    `json:"fecha"`
    Alumno      string    `json:"alumno"`
    GrupoID     int       `json:"grupo_id"`
    Grupo       string    `json:"grupo"`
    Matricula   string    `json:"matricula"`
    Descripcion string    `json:"descripcion"`
    CreatedAt   time.Time `json:"created_at"`
}
```

**Funciones principales del modelo:**
1. `GetAllRegistros`: Obtiene todos los registros ordenados por fecha
2. `GetAllGrupos`: Obtiene todos los grupos ordenados por número
3. `CreateRegistro`: Crea un nuevo registro
4. `GetRegistrosByGrupo`: Obtiene registros filtrados por grupo
5. `GetRegistrosByFecha`: Obtiene registros filtrados por fecha

## 4. Controllers/controllers.go - Controladores

Los controladores manejan la lógica de las peticiones HTTP:

1. `GetIndex`: Muestra la página principal con todos los registros
2. `GetNuevoRegistro`: Muestra el formulario para nuevo registro
3. `PostRegistro`: Procesa la creación de un nuevo registro
4. `GetReporteGrupo`: Genera reporte por grupo
5. `GetReporteDia`: Genera reporte por día

Cada controlador:
- Recibe una conexión a la base de datos
- Retorna una función que maneja el contexto de Gin
- Procesa los datos necesarios
- Renderiza la plantilla correspondiente

## 5. Routes/routes.go - Configuración de Rutas

```go
func SetupRouter(db *sql.DB) *gin.Engine {
    r := gin.Default()
    r.LoadHTMLGlob("templates/*")

    // Definición de rutas
    r.GET("/", controllers.GetIndex(db))
    r.GET("/nuevo", controllers.GetNuevoRegistro(db))
    r.POST("/registros", controllers.PostRegistro(db))
    r.GET("/reporte/grupo/:id", controllers.GetReporteGrupo(db))
    r.GET("/reporte/dia/:fecha", controllers.GetReporteDia(db))

    return r
}
```

**Rutas definidas:**
- `/`: Página principal
- `/nuevo`: Formulario de nuevo registro
- `/registros`: (POST) Crear nuevo registro
- `/reporte/grupo/:id`: Reporte por grupo
- `/reporte/dia/:fecha`: Reporte por día

## 6. Templates - Plantillas HTML

### layout.html
- Plantilla base con estructura HTML común
- Incluye Bootstrap para estilos
- Barra de navegación
- Contenedor para el contenido específico

### index.html
- Muestra todos los registros en una tabla
- Incluye formularios para generar reportes
- Permite filtrar por grupo o fecha

Las plantillas utilizan el sistema de templates de Go con:
- `{{ define "content" }}`: Define una sección de contenido
- `{{ range .registros }}`: Itera sobre los registros
- `{{ .Campo }}`: Accede a los campos de los datos

## Características Principales del Sistema

1. **Base de Datos SQLite3:**
   - Liviana y sin necesidad de servidor
   - Esquema simple pero efectivo
   - Relaciones entre grupos y registros

2. **Framework Gin:**
   - Router HTTP eficiente
   - Manejo de middleware
   - Sistema de templates

3. **Arquitectura MVC:**
   - Modelos: Estructuras de datos y operaciones BD
   - Vistas: Plantillas HTML
   - Controladores: Lógica de negocio

4. **Bootstrap:**
   - Interfaz responsiva
   - Componentes prediseñados
   - Estilos consistentes

5. **Funcionalidades:**
   - CRUD de registros
   - Filtros por grupo y fecha
   - Reportes personalizados