# Role based Access controls

### User types:
there are two user types, there are roles associated with a user object. the two roles are
creator user, regular user.
Also there is admin user.
There will be seprate permission set in the Future like pro creator, regular creator, that will dictate who can do what.
for now all creator user can create Movie, update their movie and delete their movie.
but they need some permission. For this in the django admin panel of user service, create a creator group, attach content creator pro permissions, and add a content creator user to that group(go to user details and add them)
the regular user also should be attached to a regular user group. regular user can be in future also regular, and regular premium user.


What everyone/Regular user basic can do.
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