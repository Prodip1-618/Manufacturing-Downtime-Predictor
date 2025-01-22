from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import joblib
import os

app = Flask(__name__)

try:
    data = pd.read_csv('predictive_maintenance.csv')
    data = data.rename(columns={"Target": "Downtime_Flag"})
    print("Dataset loaded and processed successfully.")
except FileNotFoundError:
    data = None
    print("Dataset file not found. Ensure 'predictive_maintanance.csv' is in the same directory.")

model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train_model():
    global model, data

    if data is None:
        return jsonify({"error": "Dataset not found. Ensure the dataset is properly loaded."}), 400

    try:
        feature_columns = [
            'Air temperature [K]',
            'Process temperature [K]',
            'Rotational speed [rpm]',
            'Torque [Nm]',
            'Tool wear [min]'
        ]
        X = data[feature_columns]
        y = data['Downtime_Flag']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LogisticRegression()
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)

        joblib.dump(model, 'model.pkl')

        return jsonify({"message": "Model training completed", "accuracy": accuracy, "f1_score": f1}), 200
    except Exception as error:
        return jsonify({"error": f"Training failed: {str(error)}"}), 500

@app.route('/predict', methods=['POST'])
def make_prediction():
    global model

    if model is None:
        return jsonify({"error": "Model is not trained. Train the model first."}), 400

    try:
        input_data = request.json
        input_df = pd.DataFrame([input_data])

        prediction = model.predict(input_df)[0]
        confidence = np.max(model.predict_proba(input_df))

        return jsonify({"Downtime": "Yes" if prediction == 1 else "No", "Confidence": confidence}), 200
    except Exception as error:
        return jsonify({"error": f"Prediction failed: {str(error)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
