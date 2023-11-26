# run_all.py

from concurrent.futures import ThreadPoolExecutor
import subprocess

def run_server():
    subprocess.run(["python", "manage.py", "runserver", "0.0.0.0:8000"])

def run_kafka_consumer():
    subprocess.run(["python", "manage.py", "listener"])

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(run_server)
    executor.submit(run_kafka_consumer)
