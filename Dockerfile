FROM python:alpine AS base
WORKDIR /app
COPY build.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "build.py"]