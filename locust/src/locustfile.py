from data import USERS
from locust import HttpLocust, TaskSet, task, between, events
from locust import __version__ as locust_version
from os import environ
import json
import redis

redis_client = redis.StrictRedis(
    host=environ.get('REDIS_HOST', "redis"),
    port=environ.get('REDIS_PORT', 6379),
    db=environ.get('REDIS_DB', 0))


def store_user_data(**kw):
    for user in USERS:
        redis_client.rpush("users", user)


# Hook up the event listeners
events.master_start_hatching += store_user_data


class MyTaskSet(TaskSet):
    # default credencials
    user = None
    password = "strong-password"

    def on_start(self):
        self.client.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "user-agent": "locust %s" % locust_version
        }

        user = redis_client.lpop("users").decode()
        response = self.login(user)
        if response.ok:
            # set token to header
            token = json.loads(response.text)["token"]
            self.client.headers["authorization"] = "Bearer %s" % token

    def on_stop(self):
        self.logout()

    def login(self, user):
        return self.client.post("/login", json={
            "user": user,
            "password": self.password
        })

    def index(self):
        self.client.get("/")

    def logout(self):
        self.client.post("/logout")

    @task(1)
    def show_index(self):
        self.index()


class MyHttpLocust(HttpLocust):
    task_set = MyTaskSet
    wait_time = between(5, 15)
