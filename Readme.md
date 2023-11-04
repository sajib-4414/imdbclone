# IMDB Clone with Python

IMDB movie review app clone with Django REST framework backend APIs.

## Table of Contents

- [Introduction](#introduction)
- [Description](#description)
- [Installation](#installation-steps)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)

## Microservices.
Load Balancer: For development, nginx. django admin's file serving is not working right now when admin of individual services is accessed through ngninx.

Database: database per service, will try to use mysql, postgres. will try to use Redis, MongoDB for some service. 
* **Authentication**: it is a Flask, lightweight microservice, just does authentication, for now generate JWT token, and return to user. it contacts the user service through grpc for login call. Most of the API calls of all services are set to have authentication through this auth service in the nginx configuration. Planned to mgirate to Oauth2. 

Testcases written some, need to work on mocking grpc
* **User service**: handles signup of user and user profile updates. it has two servers running, grpc server for login validate, and development server for grpc
Testcases are written, both type of testcases python manage.py test and also pytest.
But it seems like running python manage.py test runs all test cases everywhere.
* **Movie service**: handles movie creation,only admin can create movies. handles watchlist creation by individual users. In future: will have cast, crew, release date, these features.
* **Comments and Discussion**: In future, will handle comments, reply, discussion.
* **Notification service**: Plan to do this in Flask. In future will send in app and email notification for comments, replies, new movies added which they might like
* **Search service**: In future, will use Apacha Elastic search to search users, reviews, comments.
* **Recommendation Engine service**: In future, will be a ML model based service to have recommendation for user.
* **admin dashboard microservice**: In future managing user accounts, content, system health, also show monitoring things.plan to build with React.
* **Frontend CLient**: in future, planning to build with React, typescript, redux toolkit.
* **Analytics microservice**: in future, planning to analyze user data and analytic dashboard to improve recomemndation engine and other things

## CI/CD, scaling planning.
* (Planned): in cloud will use docker prod file for services, use AWS ALB load balancer. 
* (Planned) Unit test for all microservices, with test when other microservices are called/events emitted.
* (Planned) Have Kafka added for event communication, with message being stored, restored.
* (Planned) there will be a master-dev branch, pushing code to master-dev branch will do testing, and ability to merge code. Could be done via Jenkins/Github Actions. 
* (Planned) pushing code from master-dev to master, will run the testing, in Jenkins/Github Actions. if code is merged, then docker container will be built, pushed to dockerhub, will deploy code to aws eks cluster. will either use aws codepipeline or jenkins to build container and push to aws eks.
* (Planned) Add Istio service Mesh.
* (Planned) Add Prometheus, Grafana.
* (Planned) Add ELK stack for logging and monitoring. 
* (Planned) plan to add Redis. Add cache to load balancer, proxy, authentication and different levels.
* (Planned) Database level: sharding, paritioning, lazy loading, indexing. 

## Documentation.
* Add swagger UI for API documentation
* Add sphinx for Project documentation

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

2. Install docker and docker compose and start docker in your computer
3. in the project directory issue command `docker compose up`

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

## How I added test
* to run test files with name `test_` and files that subclass `TestCase`, install `pytest`, `pytest-django`, and have a `pytest.ini` file in the root project directory with database settings[at minimum] and other settings. and then run pytest. I did this in `user_service`
* to run test files with tests.py, run `python manage.py test`

### How did I add Grpc microservice.
* I added Grpc through django-grpc-server framework. https://djangogrpcframework.readthedocs.io/en/latest/
* current version 0.2.1 is ONLY compatible with django 4.0.10, if you have higher django version then you have to modify some parts of the django libarary in the site packages folder.
* What the plugin does is it allows you to create
and start a grpc server, and it can accept grpc requests and send respons in the django project. 
* there is a catch, it does not by default allow you to start the django development server, when you run the `python manage.py grpcrunserver` it creates a grpc server ONLY not the django development server.
* You have two options to start the development server. One is start the grpc server with the `python manage.py grpcrunserver` in one terminal and in another terminal you can start `python manage.py runserver`, then you will be running the development server where you can listen to REST /HTTP requests. Second Option is, you create a python script to run both the commands, and run that script, thats what i did in the `user_service/runcommand.py` file.
* The question is why do we want this complex setup? because we want to run REST and grpc server in the same project, so that we can call individual methods, database tables. If you want a django project that will only listent to grpc, then you dont need to follow the two options i specified above. just start the grpc server.
* Now to add grpc code in your django rest framework project you need to do following things(ref: https://djangogrpcframework.readthedocs.io/en/latest/quickstart.html for basic example, https://djangogrpcframework.readthedocs.io/en/latest/tutorial/building_services.html the example I used):

   - first have django, djangorestframework activated in your project.
   - create a proto file, this is the protobuff file.
   - install `grpcio,djangogrpcframework, grpcio-tools`
   - add `django_grpc_framework` to your installed apps.
   - generate python file from the proto file with Python's grpc_tools (not the windows/linux's grpc tools) with this, Remember we need to generate two files, one is `pb2`, one is `pb2_grpc`, the command is
   `python -m grpc_tools.protoc --proto_path=./[this is your path to proto files] --python_out=./[path to generate python pb2 output files] --grpc_python_out=./[to generate pb2_grpc file] ./account.proto[which file in the proto path you want to choose to create python]`
   - You may want to create a serializer to validate the incoming message. you can use the `proto_serializers.ModelProtoSerializer` or `proto_serializers.ProtoSerializer` , documentation is not that good. 
   - Create service 
   - Create Hanlder either in a handler.py file or in the urls file
   - run the grpc server `python manage.py grpcrunserver --dev`, 
   - I faced significant issue with packages in the proto file. I beleive it is best to keep the proto file inside a folder, and mention it as a pacakage in the proto file. then the generated python files also will be under a package directory, and will import themselves(the pb2grpc will improt pb2) from packages. the package example is found in the building a service section of the grpc. 
   - **Limitation**: at present the generated pb2 and pb2 grpc files, i am copying them to both of the services which creates grpc server and which calls it. in future i plan to make it a library.