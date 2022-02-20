from fastapi import FastAPI

description = """
access data in JSON format from air quality devices in Aberdeen and Aberdeenshire.

## Device
get JSON data **per single device location**.
contains sensor id per device

## Query by location

You will be able to:
* **Specific location** (_not implemented_).
* **Location and distance from** (_not implemented_).
* **A rectangle area** (_not implemented_).
* Latitude and Longatude input type  e.g. 57.22  or -2.77
"""

tags_metadata = [
    {
        "name": "device",
        "description": "a air quality device ",
    },
    {
        "name": "sensor",
        "description": "a sensor located within a device",
        "externalDocs": {
            "description": "Learn about sensors",
            "url": "https://sensor.community/en/sensors/airrohr/",
        },
    },
    {
        "name": "area",
        "description": "a reactange form by four latitude and longitute",
        "externalDocs": {
            "description": "Tools to help collect lat long lat long",
            "url": "https://geojson.io/",
        },
    },
]

app = FastAPI(
    title="AirAberdeenAPI",
    description=description,
    version="0.0.1",
    terms_of_service="https://airaberdeen.org/terms/",
    contact={
        "name": "airaberdeen",
        "url": "https://airaberdeen.org",
        "email": "api@airaberdeen.org",
    },
    license_info={
        "name": "GNU 3.0",
        "url": "https://github.com/AirAberdeen/api/blob/main/LICENSE",
    },
    openapi_tags=tags_metadata,
)

@app.get("/")
async def root():
    return {"message": "Hello AIR ABERDEEN"}


@app.get("/devices/location/lat/{lat}/lon/{lon}", tags=["device"])
async def read_item(lat: float,lon: float):
    return {"devices_id": [lat, lon, 1, 2, 3]}


@app.get("/devices/area/{lat}/{lon}/{distance}", tags=["area"])
async def read_item(lat: float, lon: float, distance: int):
    return {"devices_id": [lat, lon, distance, 1, 2, 3, 4, 5, 6]}


@app.get("/devices/box/{lat1}/{lon1}/{lat2}/{lon2}")
async def read_item(lat1: float, lon1: float, lat2: float, lon2: float):
    return {"devices_id": [lat1, lon1, lat2, lon2, 1, 2, 3, 4, 5, 6, 7, 8]}


@app.get("/device/{device_id}")
async def read_item(device_id):
    return {"device_id": [device_id, 1, 2, 3, 4]}


@app.get("/device/{device_id}/sensor/{sensor_id}", tags=["sensor"])
async def read_item(device_id, sensor_id):
    return {"sensor_id": [device_id, sensor_id, 1, 2, 3, 5]}


@app.get("/device/{device_id}/sensor/{sensor_id}/timestamp/{start_id}/{end_id}")
async def read_item(device_id, sensor_id, start_id: int, end_id: int):
    return {"time_range": [device_id, sensor_id, start_id, end_id, 1, 2, 3, 4, 5, 6]}
