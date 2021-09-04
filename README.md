# Aplicación en Flask basado en un tutorial de FreeCodeCamp

Este README.md consta de las siguientes secciones:

* [Descripción de las etapas](#descripcion-de-las-etapas)

* [Requerimientos](#requerimientos) **Esta sección es la primera que debe leer** si desea seguir paso a paso lo que se encuentra en este repositorio. Esta sección brinda los elementos para preparar su entorno y llevar a cabo todas las etapas descritas en este repositorio.

## Descripcion de las etapas 

El código de este repositorio se basa en la información provista por el tutorial que se presenta en [este video](https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=91s).
El video se siguió detenidamente y la forma de mostrar el desarrollo del aplicativo es a través de etapas y cada etapa estará en un *branch* de este repositorio.
El *branch* uno es la primera etapa y de allí en adelante hasta llegar a la versión "final".

### Etapa 01 

[Enlace a etapa 01](https://github.com/josanabr/flask-introduction/tree/etapa-01).

En esta etapa se ha creado un directorio llamado `app` y en su interior se encuentra el archivo [`app.py`](app/app.py) el cual tiene la lógica de la aplicación.
Por lo pronto es un código sencillo que muestra como se construyen *web services* con Flask.

### Etapa 02

[Enlace a etapa 02](https://github.com/josanabr/flask-introduction/tree/etapa-02).

En el archivo [`app.py`](app/app.py) se ha modificado la función `index()` de modo que ahora se utiliza el método `render_template` de Flask para mostrar una página HTML en lugar de que la función retorne una sencilla cadena de caracteres.

### Etapa 03

[Enlace a etapa 03](https://github.com/josanabr/flask-introduction/tree/etapa-03).

En esta etapa se hace una modificación importante al archivo [`index.html`](app/templates/index.html) de modo que ahora se usará un archivo HTML ([`base.html`](app/templates/base.html)) como plantilla para cualquier otro archivo HTML en la aplicación.

### Etapa 04 

[Enlace a etapa 04](https://github.com/josanabr/flask-introduction/tree/etapa-04).

En esta etapa se adiciona una hoja de estilos [`main.css`](app/static/css/main.css) la cual se usa en el archivo [`base.html`](app/templates/base.html).

### Etapa 05 

[Enlace a etapa 05](https://github.com/josanabr/flask-introduction/tree/etapa-05).

En esta etapa se modifica el archivo [`app.py`](app/app.py) y se incluye la definición de un objeto `Todo` el cual será el tipo de dato que se almacenará en la base de datos.

### Etapa 06 

En esta etapa se modifica el archivo [`index.html`](app/templates/index.html) de modo que se tendrá una tabla que permitirá mostrar las tareas que están pendientes por ser realizadas.

## Requerimientos

Este tutorial se llevó a cabo bajo un ambiente Ubuntu Linux 20.04.
Además de requerir [Python 3](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu) es necesario tener instalados `python3-pip` y `python3-virtualenv`. 
Para instalar este software se debe ejecutar el siguiente comando:

```
sudo apt update && sudo apt -y install python3-pip python3-virtualenv
```

Clonar este repositorio

```
git clone https://github.com/josanabr/flask-introduction
```

Una vez se termina la clonación de este repositorio, se genera un directorio llamado `flask-introduction`. 
Ingresar al directorio `flask-introduction`.

Ejecutar los siguientes comandos:

```
virtualenv env
source env/bin/activate
```

Se instala en este contexto las siguientes librerías de Python:

```
pip3 install flask flask-sqlalchemy
```

