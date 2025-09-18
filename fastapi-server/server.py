from fastapi import FastAPI, File, UploadFile
from model_helper import predict

app = FastAPI()

@app.post("/predict")
async def get_prediction( file: UploadFile = File(...)):
    image_bytes = await file.read()
    image_path = "temp_file.jpg"

    try:
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        prediction = predict(image_path)
        return {"Prediction : ", prediction}
    except Exception as e:
        return {"Error : ", str(e)}



