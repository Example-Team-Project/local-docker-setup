import random
import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    
    @task
    def getOneFilm(self):
        film_id = random.randint(1, 150)
        self.client.get(f"http://172.20.61.173:18180/api/v1/films/{film_id}", name="/api/v1/films/[film_id]")

    @task
    def getFirstFilms(self):
        self.client.get("http://172.29.233.138:18180/api/v1/films")

    @task
    def getFirstActors(self):
        self.client.get("http://172.29.233.138:18180/api/v1/actors")
