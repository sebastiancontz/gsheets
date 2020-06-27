# Título del Proyecto

Google sheets to pandas and plotly

## Comenzando 🚀

El setup inicial del proyecto es el siguiente

### Pre-requisitos 📋

Librerías necesarias para el proyecto

```
gspread
oauth2client
PyOpenSSL
pandas
plotly
```

Cuentas necesarias para el proyecto
```
google account
chart studio account
```

### Instalación 🔧

Los pasos necesarios para generar la integración entre google sheets y python son los siguientes

1. Instalar las siguiente librerías de python:

En la termina debemos ejecutar los siguientes comandos:

```python 
pip install gspread
pip install --upgrade oauth2client
pip install PyOpenSSL
```
2. Generar credenciales:

Esta es la parte más "compleja" del proyecto, y la que más tiempo consume, pero siguiendo los siguiente pasos será pan comido🐀

- Primero debemos ir a la [consola para desarrolladores de google](https://console.developers.google.com/cloud-resource-manager) y seleccionar `create project`. 
Para este ejemplo creare un proyecto llamado `gsheets`.
![](https://raw.githubusercontent.com/sebastiancontz/gsheets/master/assets/create_project.PNG)

- Una vez creado el proyecto, refrescamos el navegador y debiese aparecer dentro de la listas de proyectos:
![](https://github.com/sebastiancontz/gsheets/blob/master/assets/new_project.PNG?raw=true)

- Luego vamos al menu, y bajo el submenú de `APIs & Services` presionamos `Credentials`.
![](https://github.com/sebastiancontz/gsheets/blob/master/assets/credentials.PNG?raw=true)

- Nos aseguramos que dentro de los proyectos esté seleccionado el que acabamos de crear y seleccionamos `Create credentials`, eligiendo la opción `Service account`.
![](https://github.com/sebastiancontz/gsheets/blob/master/assets/credentials_3.PNG?raw=true)

- Acá le damos un nombre cualquiera, en este caso, lo nombraremos `gsheets` y le damos a `create`.
![](https://github.com/sebastiancontz/gsheets/blob/master/assets/credentials_4.PNG?raw=true)

- En el siguiente paso necesitamos seleccionar el rol `owner` y presionamos `create`
![](https://github.com/sebastiancontz/gsheets/blob/master/assets/credentials_5.PNG?raw=true)

- En tercer paso no es necesario cambiar nada, simplemente seleccionamos `done`.

- Una vez creada las credenciales, la página de `APIs & Services` se debiese ver similar a la siguiente:
![](https://github.com/sebastiancontz/gsheets/blob/master/assets/credentials_6.PNG?raw=true)

- Hacemos click en el nombre de la credencial, en mi caso, `gsheets@gsheets-281618.iam.gserviceaccount.com`, acción que desplegará un nuevo menú, en el cual debemos ir a `add key` y presionamos `create new key`.
![](https://github.com/sebastiancontz/gsheets/blob/master/assets/credentials_7.PNG?raw=true)

- El formato que debemos seleccionar es `json` y presionamos `create`, acción que generará una descarga automática de nuestra key en formato json. ⚠ _Importante destacar que si perdemos este archivo perderemos el acceso a nuestro proyecto, por lo cual es importante manterlo respaldado_ ⚠

- Finalmente debemos mover este archivo json a la carpeta donde está nuestro proyecto de python.

3. Una vez descargado el archivo json y fijado en la carpeta de nuestro proyecto, debemos abrir este archivo json y obtener el campo `client_email`, en el caso de nuestro ejemplo es `gsheets@gsheets-281618.iam.gserviceaccount.com`.

4. Ahora que ya contamos con nuestras credenciales y cliente email del proyecto, debemos ir a la hoja de google sheets que deseamos importar a python, y compartirla con el `client_email` recientemente obtenido.

5. Si seguimos los pasos anteriores estaremos listos para comenzar la lectura de nuestro archivo google sheet en python.

6. Para facilitar la tarea de lectura de archivo, incorporé el módulo `import_gsheets.py`, el cual incluye algunas funciones para realizar las tareas básicas, el cual debemos simplemente setear el nombre de nuestro archivo json descargado por el valor de la constante `JSON_CRED`.

```python
JSON_CRED = 'archivo_descargado.json'
```

7. Para hacer uso de las funciones, solo debemos importarla dentro de nuestro archivo de trabajo, esto lo realizamos de la siguiente manera:

```python 
import import_gsheets as gs
```
Y haremos uso de las funciones de la siguiente manera:
+ Para revisar las hojas de un workbook:

```python
import import_gsheets as gs

print(gs.get_gsheets('titanic'))
```

+ Para importar una hoja de un workbook:

```python
import import_gsheets as gs
import pandas as pd

df = gs.import_gsheet('titanic')
print(df.head())
```
