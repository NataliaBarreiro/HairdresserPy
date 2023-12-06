#Archivo a ejecutar para prender el backend
import os
from flask import Flask
from BD.connection import NataBD
from routes.route import Api

app = Flask(__name__)
# Versión actual del backend
version = "1.18.0"

# Registrar las rutas definidas en el Blueprint "Api"
app.register_blueprint(Api)

# Verificar si este archivo es el punto de entrada principal
if __name__ == "__main__":
    # Configuración para ejecutar la aplicación Flask
    app.run(debug=True, host="0.0.0.0",
            port=int(os.environ.get("PORT", 8297)))