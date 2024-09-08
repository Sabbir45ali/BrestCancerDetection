import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, render_template

app = Flask(__name__)
model = joblib.load("breastCancerModel.joblib")

@app.route('/')
def signup():
    return render_template("signup.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    input_features.append(0.0)
    
    features_value = [np.array(input_features)]
    features_name = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 
                     'smoothness_mean', 'compactness_mean', 'concavity_mean', 'missing_feature_name']
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)[0]
    if output == 0:
        return render_template("yes.html", prediction_text="Malignant (Cancer Detected)")
    else:
        return render_template("no.html", prediction_text="Benign (No Cancer Detected)")

if __name__ == "__main__":
    app.run(debug=True, port=3000)
