"""
insertar_estudiante.py
Controlador que agrega un nuevo estudiante al final de la fila (POST /agregar).
"""

from flask import request, redirect, url_for, flash
from controllers.conexion import obtener_conexion


def insertar_estudiante():
    matricula = request.form.get('matricula', '').strip()
    nombre = request.form.get('nombre', '').strip()
    carrera = request.form.get('carrera', '').strip()
    tramite = request.form.get('tramite', '').strip()

    if not matricula or not nombre or not carrera or not tramite:
        flash('Por favor llena todos los campos.')
        return redirect(url_for('index'))

    conexion = obtener_conexion()
    conexion.execute(
        'INSERT INTO fila (matricula, nombre, carrera, tramite) VALUES (?, ?, ?, ?);',
        (matricula, nombre, carrera, tramite)
    )
    conexion.commit()
    conexion.close()

    flash(f'Estudiante "{nombre}" agregado a la fila.')
    return redirect(url_for('index'))
