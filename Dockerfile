FROM python:3.9.19-slim

WORKDIR /api

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV MINIO_ACCESS_KEY: "minioadmin"
ENV MINIO_SECRET_KEY: "minioadmin"


CMD ["python3", "api/app.py"]