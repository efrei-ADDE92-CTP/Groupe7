# flask api for the model
from flask import Flask, request, jsonify
import joblib
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from prometheus_flask_exporter import PrometheusMetrics
import logging

def load_model():
    return joblib.load('knn.joblib')

def predict_model(model, data):
    return model.predict(data)[0]

def predict_from_json(model, json_data):
    data = np.array(list(json_data.values())).reshape(1, -1)
    return predict_model(model, data)

# create flask app
app = Flask(__name__)
model = load_model()

metrics = PrometheusMetrics(app)

# # Apply the same metric to all of the endpoints
# endpoint_counter = metrics.counter(
#     'Response counter', 'Request count by endpoints',
#     labels={'Response': lambda: request.res}
# )

# predict endpoint
@app.route('/predict', methods=['POST'])
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path',
                   labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def predict():
    # get data from request
    data = request.get_json()
    # predict
    prediction = predict_from_json(model, data)
    # return response
    return jsonify({'prediction': prediction})



if __name__ == "__main__":
       app.run(host='0.0.0.0', threaded=True,port=5000)