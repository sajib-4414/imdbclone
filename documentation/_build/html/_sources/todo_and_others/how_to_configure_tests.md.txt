# Configure and Run Tests
- to run test files with name `test_` and files that subclass `TestCase`, install `pytest`, `pytest-django`, and have a `pytest.ini` file in the root project directory with database settings[at minimum] and other settings. and then run `pytest`. I did this in `user_service`
- to run test files with tests.py, run `python manage.py test`
- But looks like after configuring Pytest, with `python manage.py test` all tests are running.
- Tests are per microservices, so do these things or run tests in each microservices.