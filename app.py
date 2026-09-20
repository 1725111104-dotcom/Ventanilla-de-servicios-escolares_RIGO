"""
app.py
Punto de entrada de la aplicación.
Crea la app de Flask, se asegura de que la base de datos exista,
y conecta cada ruta (URL) con su controlador.
"""

from flask import Flask

from controllers.index import index
from controllers.insertar_estudiante import insertar_estudiante
from controllers.atender_estudiante import atender_estudiante
from controllers.utilidades import inicializar_bd

app = Flask(__name__, template_folder='views')
app.secret_key = 'clave-secreta-para-mensajes'  # necesaria para usar flash()

# Nos aseguramos de que sql/fila.db y la tabla "fila" existan antes de arrancar
inicializar_bd()

# Rutas -> Controladores
app.add_url_rule('/', 'index', index, methods=['GET'])
app.add_url_rule('/agregar', 'agregar', insertar_estudiante, methods=['POST'])
app.add_url_rule('/atender', 'atender', atender_estudiante, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
