# flask api for the model
from flask import Flask, request, jsonify
import joblib
import numpy as np

def load_model():
    return joblib.load('../../models/knn.joblib')

def predict_model(model, data):
    return model.predict(data)[0]

def predict_from_json(model, json_data):
    data = np.array(list(json_data.values())).reshape(1, -1)
    return predict_model(model, data)

# create flask app
app = Flask(__name__)
model = load_model()

# predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # get data from request
    data = request.get_json()
    # predict
    prediction = predict_from_json(model, data)
    # return response
    return jsonify({'prediction': prediction})



