import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

flask_app = Flask(__name__)
model = pickle.load(open("phishing.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

# Corrected route with 'GET' method
@flask_app.route('/predict/<feature>', methods=['GET'])
def predict(feature):
    X_predict = [str(feature)]
    y_Predict = model.predict(X_predict)
    
    # Adjusting comparison for predicted output
    if y_Predict[0] == 'bad':
        result = "This is a BAD Site"
    else:
        result = "This is a GOOD Site"
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    flask_app.run(debug=True)
