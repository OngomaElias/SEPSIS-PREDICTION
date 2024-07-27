from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class SepsisFeatures(BaseModel):
    PRG: float
    PL: float
    PR: float
    SK: float
    TS: float
    M11: float
    BD2: float
    Age: float
    Insurance: int

@app.get('/')
def status_check():
    return {"Status": "API is online..."}

# Load the models
support_vector_pipeline = joblib.load('./Support_vector_pipeline.joblib')
gradient_boost_pipeline = joblib.load('./Gradient_boost_pipeline.joblib')
random_forest_pipeline = joblib.load('./Random_forest_pipeline.joblib')
encoder = joblib.load('./encoder.joblib')

@app.post('/support_vector_prediction')
def predict_patient_sepsis_status(data: SepsisFeatures):
    df = pd.DataFrame([data.model_dump()])
    prediction = support_vector_pipeline.predict(df)
    prediction = int(prediction[0])
    prediction = encoder.inverse_transform([prediction])[0]
    return {"prediction": prediction}

@app.post('/gradient_boost_prediction')
def predict_patient_sepsis_status(data: SepsisFeatures):
    df = pd.DataFrame([data.model_dump()])
    prediction = gradient_boost_pipeline.predict(df)
    prediction = int(prediction[0])
    prediction = encoder.inverse_transform([prediction])[0]
    return {"prediction": prediction}

@app.post('/random_forest_prediction')
def predict_patient_sepsis_status(data: SepsisFeatures):
    df = pd.DataFrame([data.model_dump()])
    prediction = random_forest_pipeline.predict(df)
    prediction = int(prediction[0])
    prediction = encoder.inverse_transform([prediction])[0]
    return {"prediction": prediction}
