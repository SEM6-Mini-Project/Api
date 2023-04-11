import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route('/predict', methods=['POST'])
# def predict():
#     float_features = [float(x) for x in request.form.values()]
#     print("Float features:", float_features)
#     features = [np.array(float_features)]
#     print("Features:", features)
#     prediction = model.predict(features)
#     print("Prediction:", prediction)
#     return render_template("index.html", prediction_text="The Company Bankruptcy prediction is {}".format(prediction))

def predict():
    data = request.get_json()
    input_data = [    float(data['input_1']),
        float(data['input_2']),
        float(data['input_3']),
        float(data['input_4']),
        float(data['input_5']),
        float(data['input_6']),
        float(data['input_7']),
        float(data['input_8']),
        float(data['input_9']),
        float(data['input_10']),
        float(data['input_11']),
        float(data['input_12']),
        float(data['input_13']),
        float(data['input_14']),
        float(data['input_15']),
        float(data['input_16']),
        float(data['input_17']),
        float(data['input_18'])
]

    print("Input data:", input_data)
    features = [np.array(input_data)]
    print(features)
    prediction = model.predict(features)
    print("Prediction:", prediction)
    if prediction[0]==0:
        prediction_text="The company will not go Bankrupt"
    else:
        prediction_text="The company has a high chance of going bankrupt"
    response = {'prediction': prediction_text}
    print("Response:", response)
    return jsonify(response)


if __name__ == "__main__":
    flask_app.run(debug=True)