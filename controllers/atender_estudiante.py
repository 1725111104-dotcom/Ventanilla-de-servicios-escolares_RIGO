"""
atender_estudiante.py
Controlador que atiende (saca) al estudiante que está al frente de la
fila (POST /atender). El "frente" es siempre el id más chico -> PEPS.
"""

from flask import redirect, url_for, flash
from controllers.conexion import obtener_conexion


def atender_estudiante():
    conexion = obtener_conexion()

    al_frente = conexion.execute(
        'SELECT id, nombre, tramite FROM fila ORDER BY id ASC LIMIT 1;'
    ).fetchone()

    if al_frente is None:
        conexion.close()
        flash('La fila está vacía, no hay nadie que atender.')
        return redirect(url_for('index'))

    conexion.execute('DELETE FROM fila WHERE id = ?;', (al_frente['id'],))
    conexion.commit()
    conexion.close()

    flash(f'Se atendió a "{al_frente["nombre"]}" (trámite: {al_frente["tramite"]}).')
    return redirect(url_for('index'))
