# Manufacturing-Downtime-Predictor

# Predictive Analysis for Manufacturing Operations

## Overview
This project provides a RESTful API for predictive analysis in manufacturing operations. The API predicts machine downtime or production defects based on input data. It includes endpoints to upload data, train a machine learning model, and make predictions.

## Features
1. **Upload Dataset**: Upload manufacturing data in CSV format.
2. **Train Model**: Train a Logistic Regression model to predict downtime.
3. **Make Predictions**: Predict machine downtime with confidence scores.

## Setup Instructions
### Prerequisites
- Python 3.8 or higher
- Flask
- scikit-learn
- pandas
- numpy

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Access the API at `http://127.0.0.1:5000/`.

## Endpoints
### 1. Upload Data
**POST /upload**
- Upload a CSV file with the required dataset.

### 2. Train Model
**POST /train**
- Train the Logistic Regression model.
- Returns:
  ```json
  {
    "message": "Model training completed",
    "accuracy": 0.95,
    "f1_score": 0.92
  }
  ```

### 3. Make Predictions
**POST /predict**
- Input JSON:
  ```json
  {
    "Air temperature [K]": 300,
    "Process temperature [K]": 350,
    "Rotational speed [rpm]": 1500,
    "Torque [Nm]": 20,
    "Tool wear [min]": 50
  }
  ```
- Response:
  ```json
  {
    "Downtime": "No",
    "Confidence": 1.0
  }
  ```

## Example Testing
 ## Using curl
**Train Model**:
```bash
curl -X POST http://127.0.0.1:5000/train
```
Make Predictions**:
```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"Air temperature [K]": 300, "Process temperature [K]": 350, "Rotational speed [rpm]": 1500, "Torque [Nm]": 20, "Tool wear [min]": 50}'
```

 Using Postman
1. Train Model:
   - Method: POST
   - URL: `http://127.0.0.1:5000/train`
   - Body: None

2. Make Predictions**:
   - Method: POST
   - URL: `http://127.0.0.1:5000/predict`
   - Body (JSON):
     ```json
     {
       "Air temperature [K]": 300,
       "Process temperature [K]": 350,
       "Rotational speed [rpm]": 1500,
       "Torque [Nm]": 20,
       "Tool wear [min]": 50
     }
     ```

## Files
- `app.py`: The Flask application.
- `predictive_maintanance.csv`: Sample dataset.
- `requirements.txt`: List of dependencies.

## Future Improvements
- Add a `/upload` endpoint to allow CSV uploads dynamically.
- Improve model performance using advanced algorithms.
- Deploy the API to a cloud platform for public access.

## License
This project is open-source and available under the MIT License.

---
Let me know if you need help with further enhancements or deploying the project!

