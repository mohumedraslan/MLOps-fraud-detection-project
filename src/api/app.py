!pip install fastapi uvicorn gdown joblib pandas xgboost
 
 from fastapi import FastAPI, HTTPException
 from pydantic import BaseModel
 import joblib
 import pandas as pd
 import gdown
 import os
 
 app = FastAPI()
 
 # Download model from Google Drive
 
 model_file = 'fraud_model_xgb.pkl'
 if not os.path.exists(model_file):
     file_id = '1Gm7AukV6d2wyqX1y2nBWhjpnpK7mH8ob'
     url = f'https://drive.google.com/uc?id={file_id}'
     gdown.download(url, model_file, quiet=False)
 
 # Load model
 model = joblib.load(model_file)
 
 # Define input schema
 class TransactionInput(BaseModel):
     Time: float
     V1: float
     V2: float
     V3: float
     V4: float
     V5: float
     V6: float
     V7: float
     V8: float
     V9: float
     V10: float
     V11: float
     V12: float
     V13: float
     V14: float
     V15: float
     V16: float
     V17: float
     V18: float
     V19: float
     V20: float
     V21: float
     V22: float
     V23: float
     V24: float
     V25: float
     V26: float
     V27: float
     V28: float
     Amount: float
 
 @app.post("/predict")
 async def predict(input: TransactionInput):
     try:
         data = pd.DataFrame([input.dict()])
         prediction = model.predict(data)[0]
         probability = model.predict_proba(data)[0][1]
         return {"prediction": int(prediction), "probability": float(probability)}
     except Exception as e:
         raise HTTPException(status_code=500, detail=str(e))
