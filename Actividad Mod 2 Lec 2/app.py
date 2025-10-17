from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET /info - Devuelve información básica sobre la aplicación
@app.route("/info", methods=["GET"])
def info():
    informacion = {
        "nombre": "API del Proyecto Capstone",
        "version": "1.0",
        "descripcion": "Servidor Flask para el proyecto final",
        "desarrollador": "Ezequiel Serrano Medina",
        "endpoints_disponibles": [
            "GET /info",
            "POST /mensaje"
        ]
    }
    return jsonify(informacion)

# Ruta POST /mensaje - Recibe un mensaje y devuelve respuesta personalizada
@app.route("/mensaje", methods=["POST"])
def mensaje():
    # Verificar que se envió JSON
    if not request.is_json:
        return jsonify({"error": "El contenido debe ser JSON"}), 400
    
    data = request.get_json()
    
    # Obtener el mensaje del JSON
    mensaje_recibido = data.get("mensaje", "")
    nombre = data.get("nombre", "Usuario")
    
    if not mensaje_recibido:
        return jsonify({"error": "El campo 'mensaje' es requerido"}), 400
    
    # Crear respuesta personalizada
    respuesta = {
        "estado": "mensaje_recibido",
        "saludo": f"Hola {nombre}!",
        "tu_mensaje": mensaje_recibido,
        "longitud_mensaje": len(mensaje_recibido),
        "timestamp": "2024-01-01 12:00:00"  # En una app real, usarías datetime
    }
    
    return jsonify(respuesta), 201

# Ruta principal
@app.route("/")
def home():
    return jsonify({
        "mensaje": "Bienvenido al servidor Flask del Proyecto Capstone",
        "instrucciones": "Usa /info (GET) o /mensaje (POST)"
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
