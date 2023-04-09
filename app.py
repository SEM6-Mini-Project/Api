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
    input_data = [data['input_1'], data['input_2'], data['input_3'], data['input_4'], data['input_5'], data['input_6'], data['input_7'], data['input_8'], data['input_9'], data['input_10'], data['input_11'], data['input_12'], data['input_13'], data['input_14'], data['input_15'], data['input_16'], data['input_17'], data['input_18']]
    print("Input data:", input_data)

    float_data = []
    for item in input_data:
        float_data.append(float(item))
    print(float_data)
    features = [np.array(float_data)]
    # input_array = np.array(features).reshape(1, -1)
    # input_array = np.array(input_data).reshape(1, -1)
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