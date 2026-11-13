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

    return render_template(
        'compra.html',
        titulo='Compra',
        subtotal=subtotal,
        descuento=descuento,
        total=total,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, port=5050, host="0.0.0.0")