-- Script para crear la tabla de sesiones
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    tipo TEXT NOT NULL,
    duracion INTEGER NOT NULL,
    sensaciones TEXT
);
