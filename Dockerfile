FROM python:3.13-rc-slim

WORKDIR /workdir

COPY requirements-lock.txt .
RUN pip install --no-cache-dir -r requirements-lock.txt

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

