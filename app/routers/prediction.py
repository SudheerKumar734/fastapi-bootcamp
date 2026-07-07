from fastapi import APIRouter, HTTPException
from app.schemas.titanic import Passenger

import pandas as pd
import joblib

preprocesser = joblib.load("artifacts/preprocessor.pkl")
model = joblib.load("artifacts/model.pkl")

router = APIRouter()

@router.post("/")
def predict(passenger: Passenger):

    if passenger.Age < 0:
        raise HTTPException(
            status_code=400, 
            detail="Age cannot be negative"
        )
    # Convert Pydantic object to Dictionary
    input_data = passenger.model_dump()

    # Convert Dictionary to DataFrame
    input_df = pd.DataFrame([input_data])

    # Apply preprocessing
    processed_data = preprocesser.transform(input_df)

    # Make prediction
    prediction = model.predict(processed_data)
    return {"prediction": "Survived" if prediction[0] == 1 else "Did not survive"}