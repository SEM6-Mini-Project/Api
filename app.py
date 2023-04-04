import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

# def predict():
#     float_features = [float(x) for x in request.form.values()]
#     features = [np.array(float_features)]
#     prediction = model.predict(features)
#     return render_template("index.html", prediction_text="The Company Bankruptcy prediction is {}".format(prediction))

@flask_app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = [data['input_1'], data['input_2'], data['input_3'], data['input_4'], data['input_5'], data['input_6'], data['input_7'], data['input_8'], data['input_9'], data['input_10'], data['input_11'], data['input_12'], data['input_13'], data['input_14'], data['input_15'], data['input_16'], data['input_17'], data['input_18']]
    prediction = model.predict([input_data])
    print(prediction)
    if prediction==[0]:
        prediction_text="The Company Bankruptcy prediction is not bankrupt"
    else:
        prediction_text="The Company Bankruptcy prediction is bankrupt"
    response = {'prediction': prediction_text}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
