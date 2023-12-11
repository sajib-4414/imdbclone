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

# Make port 8008 available to the world outside this container
EXPOSE 8008

# CMD ["bash", "-c", "while !</dev/tcp/notification-db/5432; do sleep 1; done; uvicorn app.main:app --host 0.0.0.0 --port 8008 --debug"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8008", "--debug"]