from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Lista de marcas de coches
marcas = [
    {"id": "bmw", "nombre": "BMW", "logo": "bmw.jpg"},
    {"id": "mitsubishi", "nombre": "Mitsubishi", "logo": "mitsubishi.jpg"},
    {"id": "subaru", "nombre": "Subaru", "logo": "logosubaru.jpg"}
]

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/gallery", response_class=HTMLResponse)
def gallery(request: Request, search: str = ""):
    """
    Muestra la galería de marcas de coches, y filtra según el término de búsqueda.
    """
    # Filtrar las marcas si se ha introducido un término de búsqueda
    if search:
        marcas_filtradas = [marca for marca in marcas if search.lower() in marca["nombre"].lower()]
    else:
        marcas_filtradas = marcas
    
    return templates.TemplateResponse("gallery.html", {
        "request": request,
        "marcas": marcas_filtradas,
        "search_term": search
    })

@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/marca/{nombre_marca}", response_class=HTMLResponse)
def marca(request: Request, nombre_marca: str):
    """
    Muestra la información detallada de una marca específica.
    """
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
