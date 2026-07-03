FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml README.md /app/
COPY sensorgenome /app/sensorgenome
RUN pip install --no-cache-dir -e .
COPY data/sample /app/data/sample
EXPOSE 8000
CMD ["uvicorn", "sensorgenome.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
