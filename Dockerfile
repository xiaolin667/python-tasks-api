FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ app/
EXPOSE 5000
HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD curl -f http://localhost:5000/health || exit 1
CMD ["python", "app/api.py"]
