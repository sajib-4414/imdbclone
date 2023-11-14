.. User-Service Documentation
   :orphan:

========================================
User-Service
========================================

User-Service handles user signup and user profile updates.

- **Servers:**
  It operates on two servers:
  - gRPC server for login validation.
  - Development server for REST API calls.

- **Test Case Coverage:**
  - gRPC Testcases: Written and implemented.
  - Two types of test cases are available: `python manage.py test` and `pytest`.
  
  Note: Running `python manage.py test` executes all test cases across the entire project, no need to run command `pytest`.

Feel free to adjust this according to your specific requirements and preferences.

