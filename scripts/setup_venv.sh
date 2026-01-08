#!/usr/bin/env bash
set -e

echo "Creando entorno virtual en .venv..."
python3 -m venv .venv

if [ ! -f ".venv/bin/activate" ]; then
  echo "Error: no se encontró el entorno virtual creado." >&2
  exit 1
fi

echo "Activando entorno virtual y actualizando pip..."
. .venv/bin/activate
pip install --upgrade pip

if [ -f requirements.txt ]; then
  echo "Instalando dependencias desde requirements.txt..."
  pip install -r requirements.txt
else
  echo "Aviso: no existe requirements.txt. Ninguna dependencia instalada." >&2
fi
