"""
conexion.py
Se encarga solamente de abrir la conexión a la base de datos SQLite
(sql/fila.db). Todos los demás controladores usan esta función.
"""

import os
import sqlite3

# Ruta absoluta a sql/fila.db, sin importar desde dónde se ejecute el programa
RUTA_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_BD = os.path.join(RUTA_BASE, 'sql', 'fila.db')


def obtener_conexion():
    conexion = sqlite3.connect(RUTA_BD)
    # row_factory permite acceder a las columnas por nombre, ej: fila['nombre']
    conexion.row_factory = sqlite3.Row
    return conexion
