FROM python:alpine3.10

ADD requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

ADD ./server/ /app/server

EXPOSE 80
ENV PORT=80
CMD ["python", "-m", "server.app"]
