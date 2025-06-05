From python:3.8-slim-buster

Run apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requerments.txt

CMD [ "python3", "app.py"]

