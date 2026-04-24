## Capítulo 1: Introducción a Git

### ¿Qué es Git?

Git es un **sistema de control de versiones distribuido**. Ayuda a los desarrolladores a **rastrear los cambios en el código fuente**, permitiéndoles trabajar de manera colaborativa y mantener un historial de versiones de su proyecto. Esto facilita regresar a versiones anteriores y ver exactamente qué ha cambiado y cuándo.

### ¿Por qué usar Git?

Git permite:

- **Control de versiones**: Guardar diferentes versiones de un proyecto, facilitando la recuperación de versiones anteriores.
- **Colaboración**: Varios desarrolladores pueden trabajar en el mismo proyecto simultáneamente.
- **Rastreabilidad**: Cada cambio tiene un historial claro, con información sobre quién hizo qué y por qué.

### Diferencia entre Git y GitHub

- **Git** es el sistema de control de versiones que se usa localmente en la computadora.
- **GitHub** es una plataforma en línea que permite alojar repositorios de Git, facilitando la colaboración remota.

### Instalación y Configuración Inicial de Git

1. **Instalación de Git**:
    
    - **Windows**: Descargar desde [git-scm.com](https://git-scm.com/).
    - **Mac**: Git ya viene preinstalado, pero puedes actualizarlo con `brew install git` si tienes Homebrew.
    - **Linux**: Instalar con `sudo apt install git` en distribuciones basadas en Debian o `sudo yum install git` en Red Hat.
2. **Configuración Inicial**: Después de instalar Git, configurar el nombre y el correo electrónico para que Git pueda registrar los cambios correctamente.
    
    bash
    
    Copiar código
    
    `git config --global user.name "Tu Nombre" git config --global user.email "tuemail@example.com"`
    

### Ejercicio 1: Configuración de Git

1. Instala Git en tu sistema si aún no lo tienes.
2. Configura tu nombre y correo electrónico siguiendo los pasos anteriores.

---

## Capítulo 2: Primeros Pasos en Git: Iniciar un Repositorio y Comandos Básicos

### Crear un Repositorio Local

Para empezar a usar Git, debes inicializar un repositorio en la carpeta de tu proyecto. Esto crea una carpeta oculta `.git` que almacena el historial del proyecto.

bash

Copiar código

`git init`

### Agregar Archivos y Hacer Commits

1. **Agregar archivos al área de preparación**: Usa `git add` para preparar archivos antes de confirmar los cambios.
    
    bash
    
    Copiar código
    
    `git add nombre_del_archivo`
    
2. **Hacer un commit**: Guarda los cambios en el historial de Git con `git commit -m "Mensaje del commit"`.
    
    bash
    
    Copiar código
    
    `git commit -m "Agregar archivo inicial"`
    

### Verificar el Estado y el Historial de Cambios

- **Ver el estado**: Muestra los archivos modificados y listos para el próximo commit.
    
    bash
    
    Copiar código
    
    `git status`
    
- **Ver el historial**: Muestra el historial de commits realizados.
    
    bash
    
    Copiar código
    
    `git log`
    

### Ejercicio 2: Crear un Repositorio y Hacer un Commit

1. Crea una carpeta nueva para tu proyecto y ve a esa carpeta en la terminal.
2. Inicia un repositorio con `git init`.
3. Crea un archivo de texto llamado `README.md`, agrega algún contenido y guarda el archivo.
4. Usa `git add README.md` para agregar el archivo.
5. Haz tu primer commit con `git commit -m "Agregar README inicial"`.

---

## Capítulo 3: Trabajando con Repositorios Remotos (GitHub)

### Vincular Repositorios Locales con Repositorios Remotos

Para conectar tu repositorio local con GitHub, debes agregar un "remoto".

bash

Copiar código

`git remote add origin https://github.com/usuario/repositorio.git`

### Subir Cambios a GitHub

Después de hacer un commit, puedes subirlo a GitHub con:

bash

Copiar código

`git push origin main`

### Clonar Repositorios Remotos

Para obtener una copia de un repositorio de GitHub en tu computadora:

bash

Copiar código

`git clone https://github.com/usuario/repositorio.git`

### Ejercicio 3: Crear un Repositorio en GitHub y Subir Cambios

1. Crea un repositorio en GitHub.
2. Conecta el repositorio local con el remoto en GitHub.
3. Haz un cambio en un archivo, confirma el cambio con `git commit` y luego usa `git push` para subirlo a GitHub.

---

## Capítulo 4: Trabajando con Ramas (Branches)

### Qué Son las Ramas y para Qué Sirven

Las ramas permiten crear "copias" del proyecto donde puedes probar cambios sin afectar la versión principal.

### Crear y Cambiar entre Ramas

Para crear una nueva rama:

bash

Copiar código

`git branch nombre_rama`

Para cambiar de rama:

bash

Copiar código

`git checkout nombre_rama`

### Fusionar Ramas (Merging)

Para unir los cambios de una rama a otra:

bash

Copiar código

`git merge nombre_rama`

### Resolver Conflictos de Fusión

Si hay cambios contradictorios, Git solicitará que resuelvas los conflictos manualmente en el archivo afectado.

### Ejercicio 4: Crear y Fusionar una Rama

1. Crea una rama llamada `nueva_funcionalidad`.
2. Haz un cambio en esta rama, confírmalo y fusiónalo en la rama principal.

---

## Capítulo 5: Versionado de Documentos en Git (Word, Excel, PowerPoint)

### Preparación y Configuración de un Repositorio para Documentos

Crea un repositorio específico para documentos de Word, Excel y PowerPoint.

bash

Copiar código

`git init documentos`

### Subir y Versionar Documentos

Usa `git add`, `git commit` y `git push` para hacer el seguimiento de estos archivos.

### Comparación de Versiones

Para comparar versiones, usa mensajes de commit detallados, ya que Git no puede mostrar diferencias internas en archivos binarios.

### Ejercicio 5: Crear un Repositorio para Documentos y Versionar un Archivo de Word

1. Crea un archivo de Word, guárdalo y agrégalo al repositorio.
2. Realiza cambios, haz commits y observa cómo se almacena cada versión.

---

## Capítulo 6: Buenas Prácticas y Resolución de Problemas Comunes

### Buenas Prácticas en Git

- Usa nombres claros en ramas y commits.
- Haz commits con frecuencia, pero solo cuando hayas completado algo lógico.

### Resolver Errores Comunes en Git

- **Deshacer el último commit**:
    
    bash
    
    Copiar código
    
    `git reset --soft HEAD~1`
    
- **Restaurar un archivo a una versión anterior**:
    
    bash
    
    Copiar código
    
    `git checkout nombre_del_archivo`
    

### Ejercicio 6: Resolver Problemas en Git

1. Simula un error común (por ejemplo, un commit erróneo) y practique cómo deshacer o corregir ese error.

---

## Capítulo 7: Resumen y Recursos para Profundizar

Recuerda los conceptos clave: repositorios, commits, ramas y control de versiones. Para continuar profundizando, consulta recursos como la [documentación oficial de Git](https://git-scm.com/doc), GitHub Docs y tutoriales en línea.

---

### 1. ¿Se tiene que subir solo un archivo o se pueden subir varios?

Puedes subir tanto un solo archivo como múltiples archivos al mismo tiempo. Git te da mucha flexibilidad en este aspecto.

- **Para subir un solo archivo**: Usa `git add nombre_del_archivo`. Esto prepara únicamente ese archivo para el próximo commit.
    
    bash
    
    Copiar código
    
    `git add archivo1.txt`
    
- **Para subir varios archivos**: Puedes usar `git add` con varios nombres de archivos separados por espacios, o bien `git add .` para agregar todos los cambios en el directorio actual y sus subdirectorios.
    
    bash
    
    Copiar código
    
    `git add archivo1.txt archivo2.txt # O agregar todos los archivos modificados git add .`
    

Esto es especialmente útil cuando tienes un proyecto con muchos archivos y quieres asegurarte de que todos se incluyan en el commit.

---

### 2. ¿Se puede subir toda la estructura de directorios?

Sí, Git puede manejar toda la estructura de directorios y archivos dentro de un proyecto. Al usar `git add .`, Git agrega toda la estructura de directorios y subdirectorios (siempre que contengan archivos) al área de preparación.

Por ejemplo:

bash

Copiar código

`git add . git commit -m "Subir estructura completa de directorios"`

Esto te permite rastrear y versionar todos los archivos y carpetas dentro de un proyecto, facilitando la administración de proyectos complejos que pueden tener múltiples directorios y archivos.

---

### 3. ¿El `git init` se inicia solo una vez por proyecto?

Sí, **`git init` se ejecuta solo una vez por proyecto**. Este comando inicializa un repositorio de Git en la carpeta actual y crea una carpeta oculta llamada `.git` donde se almacena toda la información de control de versiones para el proyecto. Una vez que has ejecutado `git init` en una carpeta, ya no es necesario volver a ejecutarlo, a menos que estés creando un nuevo proyecto.

### 4. ¿Cómo le dices a Git en qué repositorio remoto subirás los archivos?

Para indicarle a Git en qué repositorio remoto deseas subir los archivos, usas el comando `git remote add`. Esto se hace después de `git init`, solo una vez, para conectar tu repositorio local con el remoto (por ejemplo, en GitHub o GitLab).

#### Ejemplo:

Supongamos que has creado un repositorio en GitHub llamado `mi-proyecto`. Obtén la URL del repositorio (por ejemplo, `https://github.com/usuario/mi-proyecto.git`) y conéctalo de esta forma:

bash

Copiar código

`git remote add origin https://github.com/usuario/mi-proyecto.git`

Aquí, `origin` es el nombre predeterminado que Git usa para el repositorio remoto. Después de esto, puedes subir archivos usando:

bash

Copiar código

`git push origin main`

Donde `main` es la rama principal. Cada vez que hagas un commit, podrás subir los cambios a `origin` sin necesidad de volver a especificar el repositorio remoto.

---

### Resumen de los pasos típicos en un proyecto Git:

1. **Iniciar el repositorio una vez** con `git init`.
2. **Conectar el repositorio local a un repositorio remoto** (por ejemplo, en GitHub) usando `git remote add origin URL_DEL_REPOSITORIO`.
3. **Agregar archivos y hacer commits** conforme realices cambios, usando `git add` y `git commit`.
4. **Subir cambios al repositorio remoto** usando `git push origin main`.

Con esta información, puedes gestionar archivos individuales, múltiples archivos y toda la estructura de un proyecto en Git de forma efectiva. ¿Te gustaría más ejemplos prácticos o ayuda con algún comando en particular?
¡Excelente pregunta! Vamos a ver cómo Git maneja múltiples proyectos y cómo puedes indicarle a Git dónde debe ubicar cada archivo y a qué repositorio hace referencia en cada caso.

### ¿Cómo Git Ubica los Archivos en Cada Proyecto?

Git **organiza los archivos y el historial de cambios dentro de la carpeta en la que ejecutas `git init`**, creando una carpeta oculta llamada `.git`. Por lo tanto, cada carpeta de proyecto que inicializas con `git init` es un repositorio independiente.

Esto significa que, si estás trabajando en dos proyectos diferentes, por ejemplo, `proyecto1` y `proyecto2`, tendrás dos carpetas con su propio `.git`, y Git entenderá que cada archivo pertenece a su respectivo repositorio.

### Trabajar con Múltiples Repositorios Locales Simultáneamente

Si tienes dos proyectos locales, **cada proyecto tendrá su propio repositorio local** y sus archivos estarán ubicados en carpetas separadas, así:

bash

Copiar código

`/ruta/proyecto1/.git  <- repositorio de proyecto1 /ruta/proyecto2/.git  <- repositorio de proyecto2`

Entonces:

- **Para agregar archivos a `proyecto1`**, debes estar en la carpeta `/ruta/proyecto1/` en tu terminal y usar los comandos de Git desde allí.
- **Para agregar archivos a `proyecto2`**, debes cambiar de directorio a `/ruta/proyecto2/` en tu terminal y ejecutar los comandos desde esa ubicación.

### ¿Cómo Indicarle a Git a qué Repositorio Remoto Hace Referencia cada Proyecto?

Cada repositorio local puede estar vinculado a su propio repositorio remoto. Para hacerlo, solo debes especificar el repositorio remoto una vez por proyecto, y Git recordará esa referencia.

#### Paso a Paso para Configurar el Repositorio Remoto para Cada Proyecto

1. **Ubícate en la carpeta del proyecto**. Por ejemplo, si quieres trabajar en `proyecto1`:
    
    bash
    
    Copiar código
    
    `cd /ruta/proyecto1/`
    
2. **Configura el repositorio remoto** con `git remote add`. Así, especificas a qué repositorio remoto se subirán los cambios de este proyecto en particular.
    
    bash
    
    Copiar código
    
    `git remote add origin https://github.com/usuario/proyecto1.git`
    
3. Si tienes otro proyecto (`proyecto2`), ve a la carpeta de `proyecto2` y repite el proceso con la URL correspondiente.
    
    bash
    
    Copiar código
    
    `cd /ruta/proyecto2/ git remote add origin https://github.com/usuario/proyecto2.git`
    

### Ejemplo Práctico de Trabajar con Dos Proyectos en Paralelo

Supón que tienes dos proyectos, `proyecto1` y `proyecto2`, y quieres hacer commits y push a GitHub para cada uno. A continuación, te muestro cómo lo harías:

1. **Trabajar en `proyecto1`**:
    
    bash
    
    Copiar código
    
    `cd /ruta/proyecto1/ git add archivo1.txt git commit -m "Añadir archivo1 a proyecto1" git push origin main`
    
2. **Trabajar en `proyecto2`**:
    
    bash
    
    Copiar código
    
    `cd /ruta/proyecto2/ git add archivo2.txt git commit -m "Añadir archivo2 a proyecto2" git push origin main`
    

En este caso, Git sabe automáticamente a qué repositorio remoto debe hacer el push en función de la carpeta en la que te encuentras, porque configuraste `origin` para cada proyecto.

### Importante: ¿Cómo Cambiar de Proyecto sin Confusión?

Para evitar confusiones, sigue estos consejos:

- **Comprueba siempre en qué carpeta estás trabajando** con `pwd` (en Linux/Mac) o `cd` (en Windows) antes de ejecutar comandos de Git.
    
- **Verifica el remoto configurado** para cada proyecto usando el comando `git remote -v`. Esto mostrará la URL del repositorio remoto al que se suben los cambios.
    
    bash
    
    Copiar código
    
    `git remote -v`
    

Este comando es útil para confirmar que cada proyecto está correctamente vinculado a su repositorio remoto correspondiente.

### Resumen

- Cada proyecto tiene su propio repositorio local y remoto, definidos en su carpeta respectiva.
- Solo debes estar en la carpeta del proyecto para que Git gestione los archivos y el historial de ese proyecto.
- Configura el repositorio remoto una vez en cada proyecto, y Git sabrá automáticamente a dónde subir los cambios.
Git maneja las versiones de los archivos mediante **commits**, que son puntos en el tiempo donde se guardan los cambios realizados en los archivos del proyecto. Cada commit representa una versión específica del proyecto y lleva un identificador único. Este sistema permite a Git almacenar el historial completo de versiones y facilita el trabajo colaborativo, ya que cada usuario puede ver qué cambios se han realizado y quién los hizo.

Vamos a explorar cómo Git maneja las versiones de manera detallada:

### 1. **Commits: La Base del Versionado en Git**

Un **commit** es un punto de control en el tiempo, y se crea cuando ejecutas el comando `git commit`. Cada commit guarda el estado de los archivos que estaban en el área de preparación en ese momento.

- **Crear un commit**: Cuando haces un commit, Git toma una "foto" del estado de los archivos y los guarda en el historial.
    
    bash
    
    Copiar código
    
    `git commit -m "Mensaje descriptivo del cambio"`
    
- **Identificador único (hash)**: Cada commit tiene un identificador único llamado **hash**, que es una cadena alfanumérica generada automáticamente. Ejemplo:
    
    sql
    
    Copiar código
    
    `commit 3f78b6a7ac34bb4ff8453d7b6a67d08d88f3e9e2`
    

### 2. **Historial de Versiones**

Git almacena cada commit en una estructura de datos que permite ver el historial completo de versiones del proyecto. Puedes ver este historial usando el comando `git log`.

bash

Copiar código

`git log`

Este comando muestra:

- El hash de cada commit.
- El autor del commit.
- La fecha y la hora.
- El mensaje del commit.

#### Ejemplo de `git log`:

plaintext

Copiar código

`commit 3f78b6a7ac34bb4ff8453d7b6a67d08d88f3e9e2 Author: Juan Perez <juan@example.com> Date:   Wed Mar 10 14:33:37 2023 -0500      Agregar función de autenticación  commit 1a79e9a8c49c71c9b32e7f23d7b7c37d7a1f7b3e Author: Maria Garcia <maria@example.com> Date:   Tue Mar 9 12:13:10 2023 -0500      Corregir errores en la página de inicio`

### 3. **Control de Versiones Detallado con Branches (Ramas)**

En Git, puedes tener varias versiones en paralelo mediante **ramas**. Una rama es una línea de desarrollo que permite trabajar en una nueva funcionalidad o corrección sin afectar la versión principal.

- **Crear una nueva rama**: Con `git branch nombre_rama` creas una nueva rama.
- **Cambiar de rama**: Con `git checkout nombre_rama` cambias la versión activa del proyecto a esa rama.

Esto permite tener versiones separadas de un proyecto, por ejemplo, una rama `main` para la versión estable y otra llamada `feature-login` para trabajar en una nueva funcionalidad de inicio de sesión.

### 4. **Combinación de Versiones (Merge)**

Cuando finalizas el trabajo en una rama, puedes **fusionarla** (hacer un merge) con otra. Esto une los cambios de ambas ramas en una sola versión.

bash

Copiar código

`git merge nombre_rama`

Si los cambios son compatibles, Git combinará ambas versiones automáticamente. Si hay conflictos (diferencias en las mismas líneas de los archivos en ambas ramas), Git te pedirá que resuelvas el conflicto manualmente.

### 5. **Restaurar Versiones Anteriores**

Si necesitas regresar a una versión anterior, Git permite hacer un **checkout** a un commit específico o a una rama:

- **Revisar una versión anterior temporalmente**: Puedes usar `git checkout` con el hash de un commit específico para ver cómo era el proyecto en ese momento.
    
    bash
    
    Copiar código
    
    `git checkout 3f78b6a7ac34bb4ff8453d7b6a67d08d88f3e9e2`
    
- **Restaurar archivos o commits a una versión anterior permanentemente**:
    
    - Con `git reset`, puedes deshacer uno o varios commits recientes y restablecer el proyecto a un estado anterior.
        
        bash
        
        Copiar código
        
        `git reset --hard HEAD~1  # Elimina el último commit y todos los cambios`
        

### 6. **Versionado de Archivos Individuales**

Git permite versionar no solo el proyecto completo, sino también archivos individuales, por lo que puedes recuperar la versión de un archivo específico.

- **Restaurar un archivo a una versión anterior**:
    
    bash
    
    Copiar código
    
    `git checkout nombre_del_archivo`
    

Este comando devuelve el archivo a su última versión confirmada, eliminando cualquier cambio no guardado en el historial.

---

### Ejemplo Práctico del Flujo de Versionado

1. **Inicia un repositorio**:
    
    bash
    
    Copiar código
    
    `git init`
    
2. **Haz el primer commit**:
    
    bash
    
    Copiar código
    
    `echo "Primer archivo" > archivo.txt git add archivo.txt git commit -m "Agregar archivo inicial"`
    
3. **Realiza más commits**: Modifica `archivo.txt`, agrégalo y confirma los cambios.
    
4. **Consulta el historial**:
    
    bash
    
    Copiar código
    
    `git log`
    
5. **Crear una rama para una nueva funcionalidad**:
    
    bash
    
    Copiar código
    
    `git branch feature-nueva git checkout feature-nueva`
    
6. **Trabaja en la nueva funcionalidad**: Modifica `archivo.txt` y realiza commits en la rama `feature-nueva`.
    
7. **Fusiona la rama en `main`** cuando termines:
    
    bash
    
    Copiar código
    
    `git checkout main git merge feature-nueva`