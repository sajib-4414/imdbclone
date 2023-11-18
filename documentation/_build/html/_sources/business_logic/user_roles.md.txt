# Users and Roles

What everyone can do.
- Users create their account with username, email, password
- Can sign in.
- Can see any reviews, any movies.
- [Planned] See all reviews of someone.

Admin User:
- **Manage Streaming Platforms**: [Need to implement in Microservices] Only admin user creates/updates/deletes Streaming Platforms on the Movie service. Streaming Platform could be
 Netflix, Amazon Prime video, Hulu
- **Manage Movie**: [Need to implement in Microservices] Only admin user creates/updates/deletes Movie, under a specific Streaming Platform.
- **Manage Reviews**: [Need to implement in Microservices] Only admin can edit any review, otherwise it is only that user. Active field in the Review model means, the 
review is active or not. If admin changes it to False, then the review will not be counted and shown to the movie.


Authenticated Regular User
- **Posting Review**: Regular user then post a review to a movie. One user can only post one review per movie, he will be allowed to update and delete his review.
- **See Review**: Regular User can see all his reviews.