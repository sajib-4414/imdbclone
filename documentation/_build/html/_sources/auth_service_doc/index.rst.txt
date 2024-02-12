.. Auth-Service Documentation
   :orphan:

========================================
Auth-Service
========================================

Auth-Service is a FastAPI-based lightweight microservice providing central authentication for microservices.

- **Central Authentication:**
  All microservice API calls pass through the central auth API. It validates the token and then sends the username in the header to the destination microservice.
  As of 15th November 2023, decided to not raise 401 from auth service, rather pass the message to the destination service that user is not present, and let the destination handle it. 
- **Login:**
  For now generate JWT token, and return to user. it contacts the user service through grpc for validating login credentials..  

- **Handle Custom Authentication for other Django Services:**
  Important Note: There is a custom authentication file set in the Django `settings.py` file for each service. It identifies the user in the `request.user`. 
  For example, in the `movie_service`, check the `movie_service/main/custom_authentication_backend.py` file, and see how it is added as authentication in the `movie_service/main/settings.py` file.
  
  It's crucial that all microservices share the same user database. Without a shared database, access to any API of any service through the load balancer will be restricted.

- **Test Cases coverage:**
  some testcases are written, that are non GRPC related. need to work on mocking grpc to run a grpc involved test.
  
  **Migration Plan to OAuth2:**
  There is a planned migration to OAuth2 for improved security and scalability.

