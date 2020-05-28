#db dockerfile
#use version 5.7 for compatibility of python api
FROM mysql:5.7 AS db
#Mount local folder, add <src> <dest>
COPY ./data /docker-entrypoint-initdb.d
#set password
ENV MYSQL_ROOT_PASSWORD=w4sser

# Load data in databse
#SHELL ["/bin/sh", "-c"]
#RUN mysql -uroot -p"w4sser" -e"CREATE DATABASE test_db; USE test_db" &&\
#RUN mysql -uroot -p"w4sser" -t < /db/employees.sql