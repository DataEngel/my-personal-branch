# Miguel Angel Velazquez Romero

Sitio personal de presentación profesional para MLOps y Data Engineering.

## Ejecutar localmente

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
FLASK_DEBUG=1 python src/custom.py
```

Abre <http://localhost:5000>.

## Ejecutar con Docker

La imagen usa `python:3.12-slim` y ejecuta Flask como un usuario sin privilegios.

```bash
docker compose up --build
```

Abre <http://localhost:5000>.

Para detener el contenedor:

```bash
docker compose down
```

## Flujo Git

El trabajo se desarrolla en ramas `feature/*`, con integración hacia `dev` y promoción posterior a `main`.
