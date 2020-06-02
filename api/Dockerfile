#api dockerfile

FROM python:3 AS api
#Mount local folder with app files, add <src> <dest>
COPY ./dev /app

#Load data in databse
SHELL ["/bin/sh", "-c"]
RUN apt update
RUN apt install vim -y
#RUN apk add python py-pip lapack openblas-dev gcc gfortran 
RUN pip install wheel flask flask_restful numpy jsonify mysql-connector-python python-dateutil
#export flask app
ENV FLASK_APP=/app/api.py
#flas has to be started with docker exec -it <container_name> /bin/bash
# RUN flask run --host=0.0.0.0 --port=5000