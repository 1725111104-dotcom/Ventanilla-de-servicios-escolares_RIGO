-- script.sql
-- Crea la tabla "fila" si todavía no existe.
--
-- Como "id" es INTEGER PRIMARY KEY AUTOINCREMENT, siempre crece,
-- así que el estudiante con el id más chico es el que llegó primero.
-- Por eso el orden PEPS (Primeras Entradas, Primeras Salidas) se logra
-- simplemente con "ORDER BY id ASC".

CREATE TABLE IF NOT EXISTS fila (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula TEXT NOT NULL,
    nombre    TEXT NOT NULL,
    carrera   TEXT NOT NULL,
    tramite   TEXT NOT NULL
);
