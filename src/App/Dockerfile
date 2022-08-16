FROM python:3.8-slim-buster

ADD main.py .

WORKDIR /flask-app

COPY requirements.txt .

RUN  pip install gpiozero && pip install RPi.GPIO

CMD ["python", "./main.py"]