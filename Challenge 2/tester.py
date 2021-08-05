from locust import HttpUser, task, between


class APITestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def test_customers(self):
        self.client.get("http://localhost:5000/customers")

    @task(2)
    def test_stores(self):
        self.client.get("http://localhost:5000/stores")

    @task(3)
    def test_cases(self):
        self.client.get("http://localhost:5000/cases")
