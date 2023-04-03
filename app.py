import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def Home():
    return render_template("index.html")


# @app.route("/predict", methods=["POST"])
# def predict():
#     float_features = [float(x) for x in request.form.values()]
#     features = [np.array(float_features)]
#     prediction = model.predict(features)
#     return render_template("index.html", prediction_text="The Company Bankruptcy prediction is {}".format(prediction))


@app.route('/prediction', methods=['POST'])
def predict():
    X1 = request.form.get('X1')
    X2 = request.form.get('X2')
    X3 = request.form.get('X3')
    X4 = request.form.get('X4')
    X5 = request.form.get('X5')
    X6 = request.form.get('X6')
    X7 = request.form.get('X7')
    X8 = request.form.get('X8')
    X9 = request.form.get('X9')
    X10 = request.form.get('X10')
    X11 = request.form.get('X11')
    X12 = request.form.get('X12')
    X13 = request.form.get('X13')
    X14 = request.form.get('X14')
    X15 = request.form.get('X15')
    X16 = request.form.get('X16')
    X17 = request.form.get('X17')
    X18 = request.form.get('X18')

    input_query = np.array(
        [[X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18]])

    result = model.predict(input_query)[0]
    if result ==1:
        return render_template("index.html", prediction_text="The Company will Bankrupt")
    
    else:
        return render_template("index.html", prediction_text="The Company will not Bankrupt")



if __name__ == "__main__":
    app.run(debug=True)
