# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN python -m pip install --upgrade pip
# Install any needed packages specified in requirements.txt
# RUN apk update
# RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt


# Expose the port on which your Django app will run
EXPOSE 8000
EXPOSE 50051
