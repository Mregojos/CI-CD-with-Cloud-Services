FROM python:latest

WORKDIR /app
COPY . /app
VOLUME /app

RUN pip install -U -r requirements.txt

EXPOSE 80

CMD ["streamlit", "run", "app.py", "--server.port", "80"]
