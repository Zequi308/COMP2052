from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "title": "Página Principal",
        "message": "Bienvenido a mi aplicación Flask con Jinja2"
    }
    return render_template('index.html', data=data)

@app.route('/productos')
def productos():
    productos_lista = [
        {"nombre": "Laptop", "precio": 800},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Teclado", "precio": 45}
    ]
    return render_template('productos.html', productos=productos_lista)

if __name__ == '__main__':
    app.run(debug=True)
