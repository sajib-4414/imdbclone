# IMDB Movie Review Backend

IMDB movie review app clone with Django REST framework backend APIs.

## Table of Contents

- [Introduction](#introduction)
- [Description](#description)
- [Installation](#installation-steps)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)

## Introduction

For demonstraing python django based backend microservices application.

## Description
User Role:
- Users create their account with username, email, password

Admin Role:
- Only admin user creates/updates/deletes Streaming Platforms. Streaming Platform could be Netflix, Amazon Prime video, Hulu
- Only admin user creates/updates/deletes Movie, under a specific Streaming Platform.
- Only admin can edit any review, otherwise it is only that user.

Regular user:
- Regular user then post a review to a movie. One user can only post one review per movie, he will be allowed to update and delete his review.
- Regular User can see all his reviews, or all reviews of someone.
- Active field in the Review model means, the review is active or not. If admin changes it to False, then the review will not be counted and shown to the movie.


# Installation steps
1. Clone the repository:
   ``
   git clone https://github.com/your_username/your_project.git ``
2. Create a virtual environment:
```python -m venv venv```
3. Activate the virtual environment:
``source venv/bin/activate``
4. Install project dependencies:
``pip install -r requirements.txt``

## Run tests:
* Used API testcases, run ```python manage.py test <optionally-app-name>```. If no app name specified, then this code will run test cases for all apps.

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



## Technologies used

* Used Django REST framework for backend operations
* APITest cases
* Django ORM for database operations
* SQLite database, will be ugpraded to PostgreSQL database soon.
* Permissions to limit permissions to regular users wherever applicable
* Token Authentication
* Throttling to limit requests.

