from locust import HttpLocust, TaskSet, task, between

class WebsiteTasks(TaskSet):
    @task
    def getGlobalIp(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)
