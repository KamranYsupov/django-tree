FROM python:3.10

COPY requirements.txt /temp/requirements.txt

WORKDIR /django_tree
EXPOSE 8000

RUN pip install psycopg2
RUN pip install -r /temp/requirements.txt