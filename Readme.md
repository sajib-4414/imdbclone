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
* **Notification service**: Planned. Email and In app notifications.
* **Search service**: Planned. Elastic Search.
* **Recommendation Engine service**: Planned. ML recommendation.
* **admin dashboard microservice**: Planned. User, movie and all management services.
* **Frontend React Client**: built with React, typescript, redux toolkit.
* **Analytics microservice**: Planned. user data analysis from kafka.

## Technology stack:

- **Backend:** Django, FastAPI, GRPC (Django GRPC), [Planned] Flask
- **Frontend:** Webpack, React, Typescript, Redux toolkit.
- **Load Balancer** :For development, nginx. django admin's file serving is not working right now when admin of individual services is accessed through ngninx. For production will use AWS ALB load balancer.
- **Test Cases:** APITest cases, Pytest test cases, Unit test cases.
- **ORM:** Django ORM for database operations, [Planned] SQLAlchemy
- **Database:** SQLite database, will be upgraded to PostgreSQL database soon. Database: database per service, will try to use mysql, postgres. will try to use Redis, MongoDB for some service. 
- **Throttling:** Throttling to limit permissions to regular users wherever applicable
- **Authentication:** JWT Authentication, planned to upgrade to OAuth2.
- **Devops CI/CD**: Different docker for dev and prod. [Planned] jenkins/github actions for test run. [Planned] EKS Cluster deployment.

# Installation steps
1. Clone the repository:
   ``
   git clone https://github.com/your_username/your_project.git ``

2. Install docker and docker compose and start docker in your computer
3. in the project directory issue command `docker compose up`

## Run tests:
* Used API testcases, run ```python manage.py test <optionally-app-name>```. If no app name specified, then this code will run test cases for all apps. This runs all kinds of tests.

# API Endpoints

### User App Endpoints

#### User Authentication

- `POST /api/v1/login/`: Obtain an authentication token.
- `POST /api/v1/register/`: Register a new user.
- `POST /api/v1/logout/`: Log out and revoke the authentication token.

### Movie App Endpoints

#### Movies

- `GET /api/v1/`: List all movies.
- `POST /api/v1/`: Create a new movie.
- `GET /api/v1/<int:pk>/`: Retrieve details of a specific movie.
- `POST /api/v1/<int:pk>/reviews/create/`: Create a review for a specific movie.
- `GET /api/v1/<int:pk>/reviews/`: List all reviews for a specific movie.
- `GET /api/v1/reviews/<int:pk>/`: Retrieve details of a specific review.
- `GET /api/v1/list2/`: Search for movies (example endpoint).

#### Stream Platforms

- `GET /api/v1/stream/`: List all stream platforms.
- `POST /api/v1/stream/`: Create a new stream platform.
- `GET /api/v1/stream/<int:pk>/`: Retrieve details of a specific stream platform.
