#api dockerfile

FROM python:3 AS api
#Mount local folder with app files, add <src> <dest>
COPY ./dev /app

#Load data in databse
SHELL ["/bin/sh", "-c"]
#RUN apk add python py-pip lapack openblas-dev gcc gfortran 
RUN pip install wheel flask flask-api numpy jsonify mysql-connector-python
#export flask app
#RUN export FLASK_APP=/app/hello.py
#RUN flask run --host=0.0.0.0