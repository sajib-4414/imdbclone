# IMDB Clone with Python

IMDB movie review app clone with Django REST framework backend APIs.

## Table of Contents

- [Introduction](#introduction)
- [Microservices](#microservices)
- [Technologies Stack](#technology-stack)
- [Installation](#installation-steps)
- [Run tests](#run-tests)
- [API Endpoints](#api-endpoints)


## Microservices.
* **Authentication**: FastAPI app. except open API calls, all microservice API calls will pass through this. Also deals authenticaiton.
* **User service**: Django App. handles signup of user and user profile updates. Has REST, and GRPC.
* **Movie service**: Django App. handles movie related things.
* **Comments and Discussion**: Planned. Comments and replies.
* **Notification service**: Email and In app notifications.
* **Search service**: Planned. Elastic Search.
* **Recommendation Engine service**: Planned. ML recommendation.
* **admin dashboard microservice**: Planned. User, movie and all management services.
* **Frontend React Client**: built with React, typescript, redux toolkit.
* **Analytics microservice**: Planned. user data analysis from kafka.

## Technology stack:

- **Backend:** Django, FastAPI, GRPC (Django GRPC), [Planned] Flask
- **Task queue:** Celery with Redis backend in user-service
- **Frontend:** Webpack, React, Typescript, Redux toolkit.
- **Load Balancer** :For development, nginx. django admin's file serving is not working right now when admin of individual services is accessed through ngninx. For production will use AWS ALB load balancer.
- **Test Cases:** APITest cases, Pytest test cases, Unit test cases.
- **ORM:** Django ORM for database operations, SQLAlchemy, Tortoise ORM
- **Database:**  PostgreSQL database . Database: database per service,  will try to use Redis, MongoDB for some service. 
- **Throttling:** Throttling to limit permissions to regular users wherever applicable
- **Authentication:** JWT Authentication, planned to upgrade to OAuth2.
- **Devops CI/CD**: Different docker for dev and prod. [Planned] jenkins/github actions for test run. [Planned] EKS Cluster deployment.

# Installation steps
1. Clone the repository:
   ``
   git clone https://github.com/your_username/your_project.git ``

2. Install docker and docker compose and start docker in your computer. if needed install make utilities in linux/windows.
jenkins need specific permission on the mapping volume folders in the host,this is covered in the makefile.
3. in the project directory issue command `make up`

## Run tests:
* Used API testcases, run ```python manage.py test <optionally-app-name>```. If no app name specified, then this code will run test cases for all apps. This runs all kinds of tests.

# API Endpoints

### Auth service endpoints

- `GET localhost:8005/`: Root path, being called for every request.Verifies a token.
- `POST localhost:8005/auth-service/login`: login and returns a JWT token. -> for external login.
- `POST /token/create/`: Creates a new token given user email, and username. -> internal purpose only. It is called by the user-service.
- `POST /token/refresh`: Refreshes the jwt token

### User service endpoints
- `POST localhost:8005/user-service/api/v1/register`: Registers and returns a JWT token. -> for external registration.
- `POST localhost:8005/user-service/api/v1/login-validate/`: It was meant to be called by the auth service to validate credentials and let the auth service know that it is a valid user. But this is Not used anymore, endpoint is there. now we are using grpc endpoint to validate it. now auth service calls grpc endpoint for this.


### Movie service endpoints

#### Movie APIs

- `GET localhost:8005/movie-service/api/v1/movies/`: List all movies.
- `POST /api/v1/movies/`: Create a new movie.
- `GET /api/v1/movies/<int:pk>/`: Retrieve details of a specific movie.
- `POST /api/v1/<int:pk>/reviews/create/`: Create a review for a specific movie.
- `GET /api/v1/<int:pk>/reviews/`: List all reviews for a specific movie.
- `GET /api/v1/reviews/<int:pk>/`: Retrieve details of a specific review.
- `GET /api/v1/list2/`: Search for movies (example endpoint).

#### Streaming Platform APIs

- `GET /api/v1/stream/`: List all stream platforms.
- `POST /api/v1/stream/`: Create a new stream platform.
- `GET /api/v1/stream/<int:pk>/`: Retrieve details of a specific stream platform.

#### general helpful commands:
- to run a command inside the docker container, 
docker compose exec jenkins-master cat `/var/jenkins_home/secrets/initialAdminPassword`
you can also go inside the container and then run the command you want, here I am just printing the password to the console.
you could have gone to the container and do cat `/var/jenkins_home/secrets/initialAdminPassword`. they are the same.
