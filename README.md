# mensajero
Send SMS over unbranded 4G router

## ¿Cómo desarrollar si instalar casi nada?
El proyetco viene con un Makefile que genera una imagen de desarrollo en Docker. Instala el intérprete de Python, crea el virtualenv e instala los módulos descriptos en una jerarquía que describo a continuación:

`requirements/prod.txt` -> Son las librerías que necesita el programa para funcionar.

`requirements/prod.txt` -> Son las librerías que se necesitan para correr los tests del programa.

`requirements/prod.txt` -> Son las librerías que ¿se necesitan? para desarrollar el programa.

`make docker-build-dev` creamos la imagen de desarrollo.
`make docker-shell` instanciamos un contenedor que ejecuta Bash
`make docker-pytest-watch` instanciamos un contenedor que ejecuta Pytest-Watch ;)
