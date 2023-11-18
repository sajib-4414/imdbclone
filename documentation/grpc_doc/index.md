# GRPC Introduction

Includes how did I add grpc. 
- GRPC needs to run a server to listen to it.
- For grpc you need two file, pb2 and pb2 grpc. 
- **Limitation**: at present the generated pb2 and pb2 grpc files, i am copying them to both of the services which creates grpc server and which calls it. in future i plan to make it a library.

<!-- ## means these are Subheadings, will be included in the sphinx home page, ### or more # are not included -->
## Libraries Used

django-grpc library.

### How to Run
* I added Grpc through django-grpc-server framework. https://djangogrpcframework.readthedocs.io/en/latest/
* current version 0.2.1 is ONLY compatible with django 4.0.10, if you have higher django version then you have to modify some parts of the django libarary in the site packages folder.
* What the plugin does is it allows you to create
and start a grpc server, and it can accept grpc requests and send respons in the django project. 
* there is a catch, it does not by default allow you to start the django development server, when you run the `python manage.py grpcrunserver` it creates a grpc server ONLY not the django development server.
* You have two options to start the development server. One is start the grpc server with the `python manage.py grpcrunserver` in one terminal and in another terminal you can start `python manage.py runserver`, then you will be running the development server where you can listen to REST /HTTP requests. Second Option is, you create a python script to run both the commands, and run that script, thats what i did in the `user_service/runcommand.py` file.
* The question is why do we want this complex setup? because we want to run REST and grpc server in the same project, so that we can call individual methods, database tables. If you want a django project that will only listent to grpc, then you dont need to follow the two options i specified above. just start the grpc server. 

### Steps to use django grpc library
Now to add grpc code in your django rest framework project you need to do following things(ref: https://djangogrpcframework.readthedocs.io/en/latest/quickstart.html for basic example, https://djangogrpcframework.readthedocs.io/en/latest/tutorial/building_services.html the example I used):
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

<!-- ## Getting Started

Instructions on how to get a copy of your project up and running on a local machine.

### Prerequisites

List any prerequisites that need to be installed and provide commands to install them.

```bash -->
<!-- npm install -->
