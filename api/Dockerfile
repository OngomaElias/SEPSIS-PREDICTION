FROM python:3.12.3

COPY requirements.txt /tmp/requirements.txt

RUN python -m pip install --timeout 300000 --no-cache-dir -r /tmp/requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 80

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]





























