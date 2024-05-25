Welcome to IMDB Clone Project's Documentation!
==============================================

Tools Used:
-----------

- **Backend:** Django, FastAPI, GRPC (Django GRPC), [Planned] Flask
- **Frontend:** Webpack, React, Typescript, Redux toolkit.
- **Load Balancer** :For development, nginx. django admin's file serving is not working right now when admin of individual services is accessed through ngninx. For production will use AWS ALB load balancer.
- **Test Cases:** APITest cases, Pytest test cases, Unit test cases.
- **ORM:** Django ORM for database operations, [Planned] SQLAlchemy
- **Database:** SQLite database, will be upgraded to PostgreSQL database soon. Database: database per service, will try to use mysql, postgres. will try to use Redis, MongoDB for some service. 
- **Throttling:** Throttling to limit permissions to regular users wherever applicable
- **Authentication:** JWT Authentication, planned to upgrade to OAuth2.
- **Devops CI/CD**: Different docker for dev and prod. Docker compose for dev. [Planned] jenkins/github actions for test run. [Planned] EKS Cluster deployment.

.. toctree::
   :maxdepth: 2
   :caption: Services:

   auth_service_doc/index
   movie_service_doc/index
   user_service_doc/index
   react_client_doc/index
   grpc_doc/index
   problem_solving_doc/index

Search and Index
==================

* :ref:`search`

Todo and Others
==================
.. toctree::
   :maxdepth: 2

   todo_and_others/services_to_be_added
   todo_and_others/documentation_tobe_added
   todo_and_others/moving_monolith_to_microservices
   todo_and_others/scaling_plan
   todo_and_others/how_to_configure_sphinx
   todo_and_others/how_to_configure_tests

Business Logic
==================
.. toctree::
   :maxdepth: 2

   business_logic/user_roles
