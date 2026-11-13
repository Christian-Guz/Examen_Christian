from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', titulo='Inicio')

@app.route('/compra', methods=["GET", "POST"])
def compra():
    subtotal = None
    descuento = None
    total = None
    error = None

    if request.method == "POST":
        try:
            cantidad = float(request.form["cantidad"])
            precio = float(request.form["precio"])
            subtotal = round(cantidad * precio, 2)
            descuento = round(subtotal * 0.10, 2) if subtotal > 1000 else 0
            total = round(subtotal - descuento, 2)
        except ValueError:
            error = "Error: Datos inválidos"

    return render_template('compra.html',titulo='Compra',subtotal=subtotal,descuento=descuento,total=total,error=error)

@app.route('/salario', methods=["GET", "POST"])
def salario():
    horas_normales = None
    horas_extra = None
    pago_normal = None
    pago_extra = None
    total = None
    error = None

    if request.method == "POST":
        try:
            horas = float(request.form["horas"])
            pago_hora = float(request.form["pago_hora"])

            if horas < 0 or pago_hora < 0:
                error = "Error: Las horas y el pago por hora no pueden ser negativos."
            else:
                if horas <= 40:
                    horas_normales = horas
                    horas_extra = 0
                else:
                    horas_normales = 40
                    horas_extra = round(horas - 40, 2)

                pago_normal = round(horas_normales * pago_hora, 2)
                pago_extra = round(horas_extra * (pago_hora * 2), 2)
                total = round(pago_normal + pago_extra, 2)
        except ValueError:
            error = "Error: Ingresa valores numéricos válidos."

    return render_template('salario.html',titulo='Salario',horas_normales=horas_normales,horas_extra=horas_extra,pago_normal=pago_normal,pago_extra=pago_extra,total=total,error=error)

@app.route('/temperatura', methods=["GET", "POST"])
def temperatura():
    celsius = None
    fahrenheit = None
    kelvin = None
    error = None

    if request.method == "POST":
        try:
            celsius = float(request.form["celsius"])

            if celsius < -273.15:
                error = "Error: La temperatura no puede ser inferior al cero absoluto (-273.15 °C)."
            else:
                fahrenheit = round((celsius * 9 / 5) + 32, 2)
                kelvin = round(celsius + 273.15, 2)
        except ValueError:
            error = "Error: Ingresa un valor numérico válido."

    return render_template('temperatura.html',titulo='Temperatura',celsius=celsius,fahrenheit=fahrenheit,kelvin=kelvin,error=error)

@app.route('/empresa')
def empresa():
    return render_template('empresa.html', titulo='Empresa')

@app.route('/servicio')
def servicio():
    return render_template('servicio.html', titulo='Servicio')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo='Contacto')

if __name__ == '__main__':
    app.run(debug=True, port=5050, host="0.0.0.0")