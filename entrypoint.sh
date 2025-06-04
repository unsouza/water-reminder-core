#!/bin/sh

set -e

echo "==> Intalando dependências ..."
pip install --no-cache-dir -r requirements.txt

echo "==> Iniciando servidor FastAPI..."
exec fastapi dev run.py --host 0.0.0.0 --port 8000