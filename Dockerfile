from python:3.12.0 as build

EXPOSE 8501

CMD mkdir -p /app

WORKDIR /app

COPY requirements.txt ./requirements.txt

COPY kr-logo.png ./kr-logo.png

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableWebsocketCompression=false"]

ENTRYPOINT ["streamlit", "run"]

CMD ["main.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableWebsocketCompression=false"]

# CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableWebsocketCompression=false"]