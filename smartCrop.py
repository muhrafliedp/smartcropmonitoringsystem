from os import write
import uvicorn
import json
import requests
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

with open("environment.json", "r") as read_file:
    environment = json.load(read_file)

with open("crops.json", "r") as read_file:
    crops = json.load(read_file)

with open("nutrients.json", "r") as read_file:
    nutrients = json.load(read_file)


app = FastAPI(title="Smart crop monitoring and recommendation")


@app.get("/")
def root():
    return ("Lest Farm !!")

@app.get("/environment")
async def read_all_data_environment():
    return environment

@app.get("/crops")
async def read_all_data_crops():
    return crops

@app.get("/nutrients")
async def read_all_data_nutrients():
    return nutrients


@app.get("/crops/{crop_id}")
async def read_crop_info(crop_id: int):
    for crop in crops['crops']:
        if crop['id'] == crop_id:
            return crop
    raise HTTPException(
        status_code=404,
        detail=f'data tidak ditemukan'
    )


@app.get("/nutrients/{nutrient_id}")
async def read_nutrient_info(nutrient_id: int):
    for nutrient in nutrients['nutrients']:
        if nutrient['id'] == nutrient_id:
            return nutrient
    raise HTTPException(
        status_code=404,
        detail=f'data tidak ditemukan'
    )

#uvicorn smartCrop:app --reload