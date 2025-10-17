from flask import Flask, jsonify, request

app = Flask(__name__)

# Almacenamiento en memoria (simulado)
usuarios = []
productos = []

# Ruta GET /info
@app.route("/info", methods=["GET"])
def info():
    data = {
        "sistema": "Gestor de Usuarios y Productos",
        "version": "1.0",
        "descripcion": "API básica para gestionar usuarios y productos usando Flask"
    }
    return jsonify(data)

# Ruta POST /crear_usuario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.json

    # Validar datos
    if not data or "nombre" not in data or "correo" not in data:
        return jsonify({"error": "Datos incompletos. Se requieren 'nombre' y 'correo'."}), 400

    # Crear usuario
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": data["nombre"],
        "correo": data["correo"]
    }
    usuarios.append(nuevo_usuario)

    return jsonify({"mensaje": "Usuario creado exitosamente!", "usuario": nuevo_usuario}), 201

# Ruta GET /usuarios
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == "__main__":
    app.run(debug=True)

# Estructura de datos propuesta (JSON)
"""
Usuario:
{
  "usuario": {
    "id": 1,
    "nombre": "Juan Pérez",
    "correo": "juan.perez@example.com",
    "fecha_registro": "2024-10-01",
    "activo": true
  }
}

Producto:
{
  "producto": {
    "id": 101,
    "nombre": "Laptop Gaming",
    "precio": 1200.00,
    "categoria": "Tecnología",
    "disponible": true,
    "stock": 15
  }
}
"""