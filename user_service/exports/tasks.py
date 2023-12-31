# tasks.py
from celery import shared_task
from time import sleep

@shared_task
def add():
    sleep(5)  # Simulating a time-consuming task
    print(" I am printing from worker.......")
    return "retrurn value from worker...."
