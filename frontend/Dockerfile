FROM python:3.12.3

COPY requirements.txt /tmp/requirements.txt

RUN python -m pip install --timeout 300000 --no-cache-dir -r /tmp/requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port", "8501"]





