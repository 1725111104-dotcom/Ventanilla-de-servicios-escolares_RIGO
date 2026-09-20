"""
utilidades.py
Funciones de apoyo que no son ni modelo puro ni una acción del usuario.
"""

import os
from controllers.conexion import obtener_conexion, RUTA_BASE


def inicializar_bd():
    """
    Crea la tabla 'fila' si todavía no existe, usando sql/script.sql.
    Se llama una vez, al arrancar la aplicación (ver app.py).
    """
    ruta_script = os.path.join(RUTA_BASE, 'sql', 'script.sql')

    conexion = obtener_conexion()
    with open(ruta_script, 'r', encoding='utf-8') as archivo:
        conexion.executescript(archivo.read())
    conexion.commit()
    conexion.close()
