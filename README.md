# Portal de Servicios

## Propósito
Aplicación web desarrollada con **Flask** y **Bootstrap 4.6** que centraliza herramientas de cálculo operativo y secciones informativas corporativas bajo una interfaz en tema oscuro. Incluye los módulos de:
- **Compra:** Cálculo de subtotales, aplicación automática de descuento del 10% en compras mayores a $1,000 y monto total.
- **Salario:** Cálculo de nómina semanal considerando hasta 40 horas ordinarias y horas adicionales pagadas al doble.
- **Temperatura:** Conversión de grados Celsius (°C) a Fahrenheit (°F) y Kelvin (K) con validación de cero absoluto.
- **Empresa, Servicios y Contacto:** Vistas informativas con misión, visión, carrusel de servicios y canales de atención.
## Requisitos para ejecución
- **Python 3.8** o superior instalado en el sistema.
- **pip** (gestor de paquetes de Python).
- **Navegador web** moderno (Chrome, Edge, Firefox, etc.).
- Conexión a internet para cargar los recursos CDN de Bootstrap 4.6, jQuery y Popper.js.
## Creación y activación del entorno virtual

1. Abre una terminal en la carpeta raíz del proyecto y crea el entorno virtual:
   python -m venv venv
2. Con el entorno virtual activo, instala las dependencias del proyecto ejecutando:
pip install -r requirements.txt
3. Inicia el servidor local de Flask ejecutando el archivo principal:
python app.py
4. Abre tu navegador e ingresa a la siguiente dirección:
http://127.0.0.1:5050