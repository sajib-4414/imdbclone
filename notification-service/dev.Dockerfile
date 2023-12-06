# Dockerfile

# pull the official docker image
FROM python:3.9-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

#PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .