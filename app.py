from flask import Flask, render_template

app = Flask(__name__)

# Página de inicio
@app.route('/')
def index():
    return render_template("index.html")

# Página "Acerca de" (Nosotros)
@app.route('/about')
def about():
    return render_template("about.html")

# Página productos
@app.route('/productos')
def productos():
    return render_template("productos.html")

# Página contacto
@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

# Ruta con parámetro dinámico
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return render_template("index.html", nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
