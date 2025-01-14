from fastapi import FastAPI, Request
<<<<<<< HEAD
=======

>>>>>>> e8a04f7724f513e8826c8b3a9a181be1a56fb2ff
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

<<<<<<< HEAD
# Cambiamos la ruta de "/gallery" a "/marcas-de-coches"
@app.get("/marcas-de-coches", response_class=HTMLResponse)
def marcas_de_coches(request: Request):
=======
@app.get("/gallery", response_class=HTMLResponse)
def gallery(request: Request):
>>>>>>> e8a04f7724f513e8826c8b3a9a181be1a56fb2ff
    return templates.TemplateResponse("gallery.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

<<<<<<< HEAD
@app.get("/marca/{nombre_marca}", response_class=HTMLResponse)
def marca(request: Request, nombre_marca: str):
    marcas_info = {
        "bmw": {
            "nombre": "BMW",
            "descripcion": "BMW es una marca alemana conocida por su lujo y rendimiento.",
            "modelos": ["E46", "E92", "F30"]
        },
        "mitsubishi": {
            "nombre": "Mitsubishi",
            "descripcion": "Mitsubishi es conocida por sus coches confiables y deportivos.",
            "modelos": ["Lancer Evolution", "Eclipse", "Outlander"]
        },
        "subaru": {
            "nombre": "Subaru",
            "descripcion": "Subaru se destaca por sus coches con tracción integral y rendimiento deportivo.",
            "modelos": ["Impreza WRX", "Forester", "BRZ"]
        }
    }

    if nombre_marca in marcas_info:
        info = marcas_info[nombre_marca]
        return templates.TemplateResponse("marca.html", {
            "request": request,
            "nombre": info["nombre"],
            "descripcion": info["descripcion"],
            "modelos": info["modelos"]
        })
    else:
        return templates.TemplateResponse("404.html", {"request": request})
=======

>>>>>>> e8a04f7724f513e8826c8b3a9a181be1a56fb2ff
