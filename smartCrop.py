from ast import Pass
import uvicorn
import json
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

with open("json/environments.json", "r") as read_file:
    environments = json.load(read_file)

with open("json/crops.json", "r") as read_file:
    crops = json.load(read_file)

with open("json/nutrients.json", "r") as read_file:
    nutrients = json.load(read_file)


app = FastAPI(title="Smart crop monitoring and recommendation")


@app.get("/")
def root():
    return ("Let's Farm !!")


@app.get("/environments")
async def read_all_data_environments():
    return environments


@app.get("/crops")
async def read_all_data_crops():
    return crops


@app.get("/nutrients")
async def read_all_data_nutrients():
    return nutrients


@app.get("/environments/{environment_id}")
async def read_environment_info(environment_id: int):
    for environment in environments['environments']:
        if environment['id'] == environment_id:
            return environment
    raise HTTPException(
        status_code=404,
        detail=f'data tidak ditemukan'
    )


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


@app.get("/nutrients_recommendation/{crops_id}")
async def nutrients_recommendation(crops_id: int):
    soilHumidWeek = 0; airHumidWeek = 0; avgWeek = 0; totalData = 0
    priorNutrients = []

    for environment in environments["environments"]:
        totalData += 1

    for environment in environments['environments']:
        if avgWeek >= (totalData - 7):
            soilHumidWeek += environment['Kelembaban Tanah (%)']
            airHumidWeek += environment['Kelembaban Udara (%)']
            avgWeek += 1
        else:
            avgWeek += 1
    
    soilHumidAvgWeek = soilHumidWeek // 7
    airHumidAvgWeek = airHumidWeek // 7

    if crops_id == 1:
        if (soilHumidAvgWeek > 30) and (airHumidAvgWeek > 80):
            priorNutrients = ["1. Pupuk Kilat", "2. Pupuk Nasa", "3. Majemuk Multipadi"]
            return priorNutrients
        else:
            priorNutrients = ["1. Multitonik Organik", "2. Nitrea", "3. Simba fertilizer", "4. Pupuk NPK"]
            return priorNutrients
    elif crops_id == 2:
        if (soilHumidAvgWeek > 30) and (airHumidAvgWeek > 80):
            priorNutrients = ["1. Pupuk Kilat", "2. Pupuk Nasa", "3. Majemuk Multipadi"]
            return priorNutrients
        else:
            priorNutrients = ["1. Multitonik Organik", "2. Nitrea", "3. Simba fertilizer", "4. Pupuk NPK"]
            return priorNutrients
    elif crops_id == 3:
        if (soilHumidAvgWeek > 30) and (airHumidAvgWeek > 80):
            priorNutrients = ["1. Pupuk Nasa", "2. Pupuk Kilat", "3. Majemuk Multipadi"]
            return priorNutrients
        else:
            priorNutrients = ["1. Multitonik Organik", "2. Nitrea", "3. Simba fertilizer", "4. Pupuk NPK"]
            return priorNutrients
    elif crops_id == 4:
        if (soilHumidAvgWeek > 30) and (airHumidAvgWeek > 80):
            priorNutrients = ["1. Majemuk Multipadi", "2. Pupuk Nasa", "3. Pupuk Kilat"]
            return priorNutrients
        else:
            priorNutrients = ["1. Pupuk NPK", "2. Nitrea", "3. Simba fertilizer", "4. Multitonik Organik"]
            return priorNutrients
    elif crops_id == 5:
        if (soilHumidAvgWeek > 30) and (airHumidAvgWeek > 80):
            priorNutrients = ["1. Pupuk Kilat", "2. Pupuk Nasa", "3. Majemuk Multipadi"]
            return priorNutrients
        else:
            priorNutrients = ["1. Simba fertilizer", "2. Nitrea", "3. Pupuk NPK", "4. Multitonik Organik"]
            return priorNutrients
    elif crops_id == 6:
        if (soilHumidAvgWeek > 30) and (airHumidAvgWeek > 80):
            priorNutrients = ["1. Pupuk NASA", "2. Pupuk Kilat", "3. Majemuk Multipadi"]
            return priorNutrients
        else:
            priorNutrients = ["1. Nitrea", "2. Multitonik Organik", "3. Pupuk NPK", "4. Simba fertilizer"]
            return priorNutrients   

    

@app.get("/crops_recommendation/{environment_id}")
async def crops_recommendation(environment_id: int):
    for environment in environments['environments']:
        if environment['id'] == environment_id:
            intensitasCahayaLingkungan = environment['Intensitas Cahaya (lux)']
            suhuLingkungan = environment['Suhu (C)']
            kelembabanUdaraLingkungan = environment['Kelembaban Udara (%)']
            kelembabanTanahLingkungan = environment['Kelembaban Tanah (%)']
            tekananUdaraLingkungan = environment['Tekanan Udara (hPa)']
            hujanLingkungan = environment['Air Hujan']

    dataCrops = []
    for crop in crops['crops']:
        nilaiMinusIntensitasCahaya = getNegativePoint(
            crop["intensitasCahayaMin"], crop["intensitasCahayaMax"], intensitasCahayaLingkungan)//10
        nilaiMinusSuhu = getNegativePoint(
            crop["suhuMin (C)"], crop["suhuMax (C)"], suhuLingkungan)
        nilaiMinusKelembabanUdara = getNegativePoint(
            crop["kelembabanUdaraMin (%)"], crop["kelembabanUdaraMax (%)"], kelembabanUdaraLingkungan)
        nilaiMinusKelembabanTanah = getNegativePoint(
            crop["kelembabanTanahMin (%)"], crop["kelembabanTanahMax (%)"], kelembabanTanahLingkungan)
        nilaiMinusTekananUdara = getNegativePoint(
            crop["tekananUdaraMin (hPa)"], crop["tekananUdaraMax (hPa)"], tekananUdaraLingkungan)
        nilaiMinusHujan = abs(crop["hujan"] - hujanLingkungan)*-10

        nilaiMinusAkhir = nilaiMinusIntensitasCahaya + \
            nilaiMinusSuhu + nilaiMinusKelembabanUdara + \
            nilaiMinusKelembabanTanah + nilaiMinusTekananUdara + nilaiMinusHujan

        dataCrop = ["" for i in range(2)]
        dataCrop[0] = crop["name"]
        dataCrop[1] = nilaiMinusAkhir
        dataCrops.append(dataCrop)
    dataCrops = sorted(dataCrops, key=lambda x: x[1], reverse=True)
    return {dataCrops[0][0], dataCrops[1][0], dataCrops[2][0], dataCrops[3][0]}


def getNegativePoint(minValue, maxValue, environmentValue):
    if (environmentValue >= minValue) and (environmentValue <= maxValue):
        return 0
    elif (environmentValue > maxValue):
        return maxValue-environmentValue
    else:
        return environmentValue-minValue


# uvicorn smartCrop:app --reload
