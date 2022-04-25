import uvicorn
import json
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

with open("json/environment.json", "r") as read_file:
    environments = json.load(read_file)

with open("json/crops.json", "r") as read_file:
    crops = json.load(read_file)

with open("json/nutrients.json", "r") as read_file:
    nutrients = json.load(read_file)


app = FastAPI(title="Smart crop monitoring and recommendation")


@app.get("/")
def root():
    return ("Let's Farm !!")


@app.get("/environment")
async def read_all_data_environment():
    return environments


@app.get("/crops")
async def read_all_data_crops():
    return crops


@app.get("/nutrients")
async def read_all_data_nutrients():
    return nutrients

@app.get("/environment/{environment_id}")
async def read_environment_info(environment_id: int):
    for env in environments['environments']:
        if env['id'] == environment_id:
            return env
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
