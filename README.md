# Aplicación en Flask basado en un tutorial de FreeCodeCamp

Este README.md consta de las siguientes secciones:

* [Descripción](#descripcion)

* [Requerimientos](#requerimientos)

## Descripción 

El código de este repositorio se basa en la información provista por el tutorial que se presenta en [este video](https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=91s).
El video se siguió detenidamente y la forma de mostrar el desarrollo del aplicativo es a través de etapas y cada etapa estará en un *branch* de este repositorio.
El *branch* uno es la primera etapa y de allí en adelante hasta llegar a la versión "final".
En cada *branch* el README.md mostrará la información en orden cronológico inverso, es decir, la descripción de la primera etapa se encontrará al final del documento y la descripción del *branch* correspondiente se ubicará en la parte superior del archivo.

Estas son todas las *branches* que al momento se han incorporado a este repositorio:

* [Etapa 01]()
* [Etapa 01]()
* [Etapa 01]()
* [Etapa 01]()
* [Etapa 01]()
* [Etapa 01]()
* [Etapa 01]()
* [Etapa 01]()
* [Etapa 01]()
* [Etapa 01]()
* [Etapa 01]()

## Requerimientos

Este tutorial se llevó a cabo bajo un ambiente Ubuntu Linux 20.04.
Además de requerir Python 3 es necesario tener instalados `python3-pip` y `python3-virtualenv`. 
Para instalar este software se debe ejecutar el siguiente comando:

```
sudo apt update && sudo apt -y install python3-pip python3-virtualenv
```

Clonar este repositorio

```
git clone 
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

