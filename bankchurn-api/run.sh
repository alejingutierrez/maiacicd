#!/bin/bash

# Script para ejecutar la aplicación FastAPI
# Basado en la configuración del Procfile

# Configurar el puerto (por defecto 8001, pero puede ser sobrescrito por variable de entorno)
PORT=${PORT:-8001}

# Ejecutar la aplicación FastAPI con Uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT
