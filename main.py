import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model/price_predictor.joblib")


class Flats(BaseModel):
    """
    Input features validation for model
    """
    totsp: int
    dist: float
    metrdist: int
    walk: int
    brick: int
    floor: int
    code: int


@app.post('/predict')
def predict(flat: Flats):
    """"
    :param flat: input data from the post request
    :return: predicted price
    """
    features = [[
        flat.totsp,
        np.log(flat.dist),
        flat.metrdist,
        flat.walk,
        flat.brick,
        flat.floor,
        flat.code
    ]]

    prediction = model.predict(features).tolist()[0]
    return {
        "prediction": np.exp(prediction)
    }


if __name__ == "__main__":
    # Run server using given host and port
    uvicorn.run(app, host='127.0.0.1', port=80)
