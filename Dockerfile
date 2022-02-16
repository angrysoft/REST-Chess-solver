FROM python:3.9

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY restchess /code/
COPY tests /code/