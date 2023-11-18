# Moving monolith to microservices.

usecase for monolith movie app to User-service+Movie_service
- **Creating table, copying data**: in the beginning it was movie review monolith app. then i created another app, 
  user_microservice with the same user table. now i copied the original app's user_table data to the user_microservice, 
  then all user related tables, i created and copied the data. then i kept just the user table as a copy database in the original app. 
- **Moving code and API paths**: I copied the code directly associated with the user table, login, signup, permission, other information
  code to user_service. I ensured testcases passed, and the user_services was working. I then slowly commented out those codes in the
  original app to make sure it is not referecing anything more than just the core user table, which is needed to map movies to users.
  When I commented everything, and tested, it all worked. Then i added the user_services to the load balancer, so that the user related api
  calls are directed to the User service.
- **Setting Custom authentication**:Now the user service should contain all user related tables. and should handle login,
  signup, but the movie service should not do those. and most importantly these databases should be in sync.
  [with event based systems, we can restream previously lost events to create missing users]. so i made sure user is only authenticatiing
  with the user_service with JWT and with that JWT token they can access movie service. movie service will recognize the jwt token
  and map it to the user of its dataabase and let user access api. (Actually, I did central authentication though, where all call
  will pass via auth_service[i further broke down user service to a user_service+stateless auth service], if yes then it will pass
  username in the header, movie service is identifying the user from the database with custom authentication file set inthe django setings).
  it will modify the request.user for every request.
- **Slowly delete code** : Now when I saw that login, signup, profile modify is done via user_service, and movie service can effectively work
  with movie releated things with its movie table and user table. I deleted the code. I also deleted the tables from the movie service's database.
  also tested the code to see all existing funcationality works or not.