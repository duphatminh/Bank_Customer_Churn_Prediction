from flask import Flask, render_template, request
import os
import keras
import numpy as np

app = Flask(__name__)
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model')
# Loading model
model = keras.models.load_model(model_path)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/About.html.html')
def Model():
    return render_template("About.html.html")

@app.route('/Data.html.html')
def Data():
    return render_template("Data.html.html")

@app.route('/Features.html.html')
def Features():
    return render_template("Features.html.html")

@app.route('/Stat.html.html')
def Statistics():
    return render_template("Stat.html.html")

@app.route('/Predict.html.html')
def Predict():
    return render_template("Predict.html.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array([int_features])]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('Predict.html.html', prediction_text='Predicted Price should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
