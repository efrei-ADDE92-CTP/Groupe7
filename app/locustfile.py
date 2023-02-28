from locust import HttpUser,task,between 

class AppUser(HttpUser):
    wait_time = between(2,5)

	# Endpoint
    @task
    def predict(self):

        self.client.post('/predict',json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        })