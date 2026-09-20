"""
index.py
Controlador de la página principal (GET /).
Consulta el estado completo de la fila y se lo manda a la vista.
"""

from flask import render_template
from controllers.conexion import obtener_conexion


def index():
    conexion = obtener_conexion()

    todos = conexion.execute(
        'SELECT id, matricula, nombre, carrera, tramite FROM fila ORDER BY id ASC;'
    ).fetchall()

    conexion.close()

    total = len(todos)
    siguiente = todos[0] if total > 0 else None
    vacia = total == 0

    return render_template(
        'index.html',
        todos=todos,
        siguiente=siguiente,
        total=total,
        vacia=vacia
    )
