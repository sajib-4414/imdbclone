from django.apps import AppConfig


class MovieAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "movie_app"
    #tried starting the consumer here, but that results in not runnign the django server
    # def ready(self):
        # import threading
        # from django.apps import apps
        # from events.consumers import start_consumer
        # start_consumer()
        # app_ready = apps.ready  # Check if apps are ready
        # if app_ready:
        #     start_consumer()
        #     # Import and start the Kafka consumer
        #     # from events.consumers import start_consumer
        #     # consumer_thread = threading.Thread(target=start_consumer)
        #     # consumer_thread.start()
        # else:
        #     print("Django apps are not ready yet. Consumer not started.")

