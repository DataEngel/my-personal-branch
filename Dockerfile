FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && addgroup --system app && adduser --system --ingroup app app

COPY . .
RUN chown -R app:app /app

USER app

EXPOSE 5000

CMD ["python", "src/custom.py"]
