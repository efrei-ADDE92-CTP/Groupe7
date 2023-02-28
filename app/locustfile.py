import random
from locust import HttpUser,task,between 

class AppUser(HttpUser):
    wait_time = between(2,5)

    #generate random deciaml number
    def on_start(self):
        self.sepal_length = round(random.uniform(4.3,7.9),1)
        self.sepal_width = round(random.uniform(2.0,4.4),1)
        self.petal_length = round(random.uniform(1.0,6.9),1)
        self.petal_width = round(random.uniform(0.1,2.5),1)

	# Endpoint
    @task
    def predict(self):
        # self.client.post('/predict',json={
        #     "sepal_length": round(random.uniform(4.3,7.9),1),
        #     "sepal_width": round(random.uniform(2.0,4.4),1),
        #     "petal_length": round(random.uniform(1.0,6.9),1),
        #     "petal_width": round(random.uniform(0.1,2.5),1)
        # })

        self.client.post('/predict',json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        })