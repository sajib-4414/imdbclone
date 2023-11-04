# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set the working directory in the container
WORKDIR /app
RUN mkdir static

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run collectstatic to collect static files
RUN python manage.py collectstatic --noinput

# for grpc starting the grpc server in the same container
# Install supervisor
RUN apt-get update && apt-get install -y supervisor

# Add the supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the port on which your Django app will run
EXPOSE 8000
EXPOSE 50051

# # Define the command to run your Django application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# CMD ["python", "runcommand.py"]
# CMD ["/usr/bin/supervisord"]