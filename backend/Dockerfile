FROM python:3.9-slim

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install libpq-dev -y \
    && apt-get install vim -y \
    && apt-get install iputils-ping -y \
    && apt-get clean

WORKDIR /app

COPY . /app/

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]

