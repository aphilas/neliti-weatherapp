from typing import Optional

import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def get_index(
    request: Request, lat: Optional[float] = None, lon: Optional[float] = None
):
    temp = None

    if lat and lon:
        r = requests.get(
            "https://api.met.no/weatherapi/locationforecast/2.0/compact",
            params=dict(lat=lat, lon=lon),
            headers={"User-Agent": "NelitiWeatherApp/0.1 github.com/aphilas"},
        )

        temp = r.json()["properties"]["timeseries"][0]["data"]["instant"]["details"][
            "air_temperature"
        ]

    params = dict(request=request)

    if temp:
        params["temp"] = temp

    return templates.TemplateResponse("index.html", params)
