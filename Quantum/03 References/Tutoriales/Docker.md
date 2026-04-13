## Tutorial de Docker: Guía Completa para Informáticos con Conocimientos Básicos

---

### 1. Introducción a Docker y sus Conceptos Clave

#### ¿Qué es Docker?

Docker es una plataforma que permite crear, gestionar y ejecutar aplicaciones en contenedores, que son entornos aislados que incluyen todos los elementos necesarios para que una aplicación se ejecute de manera consistente en cualquier sistema.

#### Contenedores vs. Máquinas Virtuales

A diferencia de las máquinas virtuales (VMs), los contenedores comparten el sistema operativo del host, lo que los hace más ligeros y eficientes en recursos. Esto permite iniciar y escalar contenedores rápidamente sin la sobrecarga de una VM completa.

#### Componentes Básicos de Docker

- **Imágenes**: Plantillas inmutables que contienen el código y las dependencias de una aplicación.
- **Contenedores**: Instancias de una imagen en ejecución. Cada contenedor se ejecuta de forma aislada y tiene su propio sistema de archivos.
- **Dockerfile**: Archivo de texto que define cómo construir una imagen.
- **Volúmenes**: Almacenamiento persistente para los datos que deben sobrevivir a los ciclos de vida de los contenedores.
- **Redes**: Configuraciones para conectar contenedores entre sí y con servicios externos.

### 2. Instalación y Configuración Básica

#### Instalación de Docker

1. **Linux**: Usar el gestor de paquetes:
    
    bash
    
    Copiar código
    
    `sudo apt-get update sudo apt-get install docker-ce docker-ce-cli containerd.io`
    
2. **Windows y macOS**: Descargar el instalador desde Docker Desktop.

#### Configuración Inicial

- Comprobar la instalación con:
    
    bash
    
    Copiar código
    
    `docker --version docker run hello-world`
    
    Esto ejecutará un contenedor básico de prueba para verificar la correcta configuración.

### 3. Comandos Básicos en Docker

#### Comandos para Gestionar Contenedores e Imágenes

- **Iniciar un contenedor**:
    
    bash
    
    Copiar código
    
    `docker run -d --name mi_contenedor nginx`
    
- **Listar contenedores**:
    
    bash
    
    Copiar código
    
    `docker ps       # Contenedores en ejecución docker ps -a    # Todos los contenedores`
    
- **Detener y eliminar contenedores**:
    
    bash
    
    Copiar código
    
    `docker stop mi_contenedor docker rm mi_contenedor`
    
- **Eliminar imágenes**:
    
    bash
    
    Copiar código
    
    `docker rmi nginx`
    

### 4. Creación de Imágenes Personalizadas

#### Introducción al Dockerfile

Un Dockerfile es un archivo que contiene instrucciones para construir una imagen. Ejemplo de un Dockerfile básico:

Dockerfile

Copiar código

`# Usa una imagen base FROM nginx:latest  # Copia archivos al contenedor COPY . /usr/share/nginx/html  # Expone el puerto EXPOSE 80  # Define el comando por defecto CMD ["nginx", "-g", "daemon off;"]`

#### Creación de una Imagen

Para construir una imagen a partir de este Dockerfile:

bash

Copiar código

`docker build -t mi_imagen .`

### 5. Gestión de Volúmenes y Persistencia de Datos

#### Concepto de Volúmenes

Los volúmenes permiten que los datos persistan fuera del ciclo de vida de un contenedor, útil para bases de datos u otras aplicaciones que requieren almacenamiento duradero.

#### Comandos para Crear y Usar Volúmenes

- **Crear un volumen**:
    
    bash
    
    Copiar código
    
    `docker volume create mi_volumen`
    
- **Montar un volumen en un contenedor**:
    
    bash
    
    Copiar código
    
    `docker run -d -v mi_volumen:/data nginx`
    

#### Ejemplo de Uso de Volúmenes

Este comando crea un volumen donde se almacenarán los datos en la carpeta `/data` del contenedor. Esto garantiza que la información sobreviva a reinicios del contenedor.

### 6. Networking en Docker

#### Redes en Docker

Las redes permiten que los contenedores se comuniquen entre sí y con el mundo exterior. Tipos de redes:

- **Bridge**: Red privada que permite la comunicación entre contenedores.
- **Host**: El contenedor comparte la red del host.
- **Overlay**: Utilizada en Swarm para conectar servicios entre nodos.

#### Comandos para Gestionar Redes

- **Crear una red personalizada**:
    
    bash
    
    Copiar código
    
    `docker network create mi_red`
    
- **Conectar un contenedor a una red**:
    
    bash
    
    Copiar código
    
    `docker run -d --network mi_red nginx`
    

#### Ejemplo Práctico

Crear una red para conectar un contenedor de aplicación con otro de base de datos.

### 7. Deployment de Contenedores

#### Preparación para Deployment

Antes del despliegue, verifica que:

- La imagen esté optimizada y ligera.
- Los Dockerfiles cumplan buenas prácticas de seguridad.

#### Deployment Local con Docker Compose

Docker Compose permite definir y ejecutar aplicaciones multi-contenedor:

yaml

Copiar código

`version: '3' services:   web:     image: nginx     ports:       - "80:80"   db:     image: mysql     environment:       MYSQL_ROOT_PASSWORD: example`

Ejecutar con:

bash

Copiar código

`docker-compose up -d`

#### Deployment en Producción

En producción, herramientas como **Docker Swarm** o **Kubernetes** pueden manejar despliegues en cluster para garantizar alta disponibilidad.

### 8. Casos de Uso y Buenas Prácticas

#### Ejemplos de Uso

1. **Desarrollo Local**: Usar Docker para encapsular todas las dependencias en contenedores, evitando conflictos en entornos locales.
2. **Despliegue de Microservicios**: Organizar cada microservicio en su contenedor.

#### Buenas Prácticas

- Mantener las imágenes ligeras.
- Limitar permisos de usuario.
- Minimizar los puertos expuestos y usar redes privadas.

### 9. Conclusión y Recursos Adicionales

#### Resumen

En este tutorial cubrimos desde los conceptos básicos hasta el despliegue de contenedores en entornos de producción. Docker permite a los desarrolladores crear entornos aislados que pueden ejecutarse de manera consistente en cualquier sistema.

#### Recursos Adicionales

- Documentación oficial de Docker
- Comunidades y foros como Stack Overflow o GitHub.


