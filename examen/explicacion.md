## Funcionamiento de la aplicación Web con Flask

El programa presente funciona desde que el usuario escribe en un navegador web el URL correspondiente de la página en donde incluye la **dirección IP** y el del **servidor** junto con el **puerto** donde se encuentra el programa, generando una petición **HTTP** al **servidor** enviando un método **GET** de solicitud.
 Este mismo busca la función de la dirección de recibió, la ejecuta armando así el **HTML** correspondiente que mostrará el **servidor**.
 Este archivo cuenta con un código **HTML** en un archivo **HTML** dentro de una carpeta llamada **templates** donde se guardan los diferentes diseños de cada página, los cuales, diseñan el modelo principal de la página, funcionando como el **Frontend** que será todo aquello que el usuario será capaz de ver e interactura con ello (Inicio, Compra, Salario, etc), junto con otros lenguajes de diseño como **CSS** y **JavaScript**. Todo este diseño está generado por un **Framework** llamado **Bootstrap** el cual permite el diseño de una página web que pueda ser adaptable para cualquier equipo electrónico además de contar con la libería de **Flask** la cual se encarga de la ejecución de la diferentes páginas.
 Con todo ello, el **servidor**, además de generar el diseño **HTML**, se encarga de responder y trabajar con los datos de los diferentes formularios con los que trabaja la página web que incluye cálculos o peticiones de información (ya sea en el cálculo de compras o el salario), cuyos datos envia el usuario a través de un método **POST** y el **servidor** trabaja con ellos utilizando el lenguaje de **Python** para su cálculo y finalmente este mismo presenta una respuesta visible para el usuario representándose esto como el **Backend** del programa que únicamente controla el **servidor**.
Una vez que el **servidor** creado el diseño **HTML** de la página responde con un método **POST** el cual depende de su número para conocer la situación de la página pudiendo ser:
- 200 | Todo salió correctamente y la página se mostrará
- 302 | Se te direccionará a otra URL
- 404 | No se encontró o no existe la dirección que se colocó
- 500 | Hay un error en el código del servidor.
Con ello el **servidor** mostrará o no el diseño **HTML** según el método enviado.

## Diagrama de ciclo Petición-Respuesta

# Cliente (Navegador)                                          #Servidor Flask
|1. Escribe el URL con la IP y puerto|------Envía un GET------>|2. Busca la función de la dirección                   |
|5. Se muetra el HTML                |                         |3. Ejecuta la función                                 |
|6. Solicita calcular una cantidad   |<--Regresa códgio 200ok--|4. Arma el HTML de la página con el modelo del archivo|
|desde el progarma                   |-----Envía un POST------>|7. Busca la función de la petición y ejecuta el       |
|8. Se muetra el resultado           |<--Retorna el resultado--|código Python para el                                 |