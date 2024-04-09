from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel

app = FastAPI()

model = load("model.pkl")
model_classes = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}


class Observation(BaseModel):
    """
    A Pydantic model for the observation data.
    This is our ML model's input data.
    """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
async def root():
    return {
        "name": "back4app-deploy-ml-model",
        "description": "A FastAPI webapp demonstrating how to deploy a ML model to Back4app Containers.",
        "version": "1.0.0",
    }


@app.post("/predict")
async def predict(observation: Observation):
    predictions = model.predict([[
        observation.sepal_length,
        observation.sepal_width,
        observation.petal_length,
        observation.petal_width,
    ]])
    prediction = predictions[0]
    prediction_class = model_classes[prediction]
    return {
        "prediction": int(prediction),
        "prediction_class": prediction_class,
    }
