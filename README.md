# Sistema de Fila - Ventanilla de Servicios Escolares

Aplicación web en **Python (Flask) + SQLite**, con arquitectura **MVC**,
para administrar la atención de estudiantes en la ventanilla de
servicios escolares siguiendo el principio **PEPS** (Primeras
Entradas, Primeras Salidas).

## ¿Qué hace el sistema?

- Agregar un estudiante a la fila
- Atender al estudiante que está al frente
- Consultar quién es el siguiente estudiante
- Mostrar todos los estudiantes que están esperando
- Contar cuántos estudiantes están esperando
- Avisar si la fila está vacía

Datos de cada estudiante: **matrícula, nombre, carrera y tipo de trámite.**

## Estructura del proyecto

```
fila-ventanilla/
├── LICENSE
├── README.md
├── app.py
├── requirements.txt
├── controllers/
│   ├── __init__.py
│   ├── conexion.py             # abre la conexión a sql/fila.db
│   ├── utilidades.py           # crea la base de datos si no existe
│   ├── index.py                # GET  /        -> muestra la fila
│   ├── insertar_estudiante.py  # POST /agregar  -> agrega a la fila
│   └── atender_estudiante.py   # POST /atender  -> atiende al frente
├── sql/
│   ├── fila.db
│   └── script.sql
└── views/
    ├── layout.html
    └── index.html
```

## ¿Cómo funciona el MVC?

1. El usuario llena el formulario o presiona "Atender siguiente" en la
   **vista** (`views/index.html`).
2. El navegador manda esa acción a una ruta de `app.py`
   (`/agregar` o `/atender`), que llama al **controlador** correspondiente.
3. El controlador ejecuta el SQL necesario contra `sql/fila.db`
   (el **modelo**, es decir, la base de datos).
4. El controlador redirige de vuelta a `/`, donde `controllers/index.py`
   vuelve a consultar la fila y se la pasa a la **vista** para mostrarla.

## ¿Cómo funciona la fila (PEPS)?

La tabla `fila` (definida en `sql/script.sql`) usa un `id` autoincremental:

```sql
CREATE TABLE IF NOT EXISTS fila (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula TEXT NOT NULL,
    nombre    TEXT NOT NULL,
    carrera   TEXT NOT NULL,
    tramite   TEXT NOT NULL
);
```

Como el `id` siempre crece, el estudiante con el `id` más chico es el
que llegó primero. Por eso:

| Acción                      | Consulta SQL                                          |
|------------------------------|--------------------------------------------------------|
| Agregar estudiante            | `INSERT INTO fila (...) VALUES (...)`                  |
| Consultar siguiente           | `SELECT ... ORDER BY id ASC LIMIT 1`                    |
| Atender siguiente             | (consulta el de arriba y luego) `DELETE FROM fila WHERE id = ?` |
| Mostrar todos los que esperan | `SELECT ... ORDER BY id ASC`                            |
| Contar estudiantes            | `SELECT COUNT(*) FROM fila`                             |
| Saber si está vacía           | Verdadero si el total es 0                              |

## Cómo ejecutarlo

Necesitas Python 3 instalado. Desde la carpeta del proyecto:

```
python3 -m venv venv
source venv/bin/activate        # en Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 app.py
```

Y abre en tu navegador: `http://127.0.0.1:5000`

La primera vez que corres `app.py`, si `sql/fila.db` no existiera, el
propio sistema la crea automáticamente usando `sql/script.sql`
(ver `controllers/utilidades.py`).

## Cómo subirlo a GitHub

```
cd fila-ventanilla
git init
git add .
git commit -m "Sistema de fila para ventanilla de servicios escolares (MVC)"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/NOMBRE-DEL-REPO.git
git push -u origin main
```

## Posibles mejoras a futuro (opcional)

- Agregar un historial de estudiantes ya atendidos (otra tabla).
- Validar que la matrícula no se repita en la fila.
- Agregar una vista para editar los datos de un estudiante en espera.
