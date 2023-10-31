# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8003 available to the world outside this container
EXPOSE 8003

# Define the command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
