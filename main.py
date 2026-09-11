from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def calcular_tiempo(anio, mes, dia, hora, minuto, segundo):
    fecha_evento = datetime(anio, mes, dia, hora, minuto, segundo)
    ahora = datetime.now()
    diferencia = ahora - fecha_evento
    total_seg = int(diferencia.total_seconds())
    anios = total_seg // (365 * 86400)
    resto = total_seg % (365 * 86400)
    dias = resto // 86400
    resto = resto % 86400
    horas = resto // 3600
    resto = resto % 3600
    minutos = resto // 60
    segundos = resto % 60
    texto_formateado = f"""{anios} años, {dias} días, {horas}h {minutos}m
    {segundos}s"""
    return texto_formateado


@app.get("/")
def inicio():
    tiempo_revolucion_industrial = calcular_tiempo(1760, 1, 1, 0, 0, 0)
    return {"mensaje": tiempo_revolucion_industrial}


@app.get("/calculo-de-duplicacion")
def tiempo_de_duplicacion():
    tiempo_calculo_de_duplicacion = calcular_tiempo(1896, 4, 1, 0, 0, 0)
    return {"mensaje": tiempo_calculo_de_duplicacion}


@app.get("/curva-keeling")
def tiempo_de_curva():
    tiempo_curva = calcular_tiempo(1958, 3, 29, 0, 0, 0)
    return {"mensaje": tiempo_curva}


@app.get("/evento")
def evento_climatico():
    tiempo_conferencia = calcular_tiempo(1979, 2, 12, 0, 0, 0)
    return {"mensaje": tiempo_conferencia}


@app.get("/fundacion_IPCC")
def organizacion_de_IPCC():
    tiempo_IPCC = calcular_tiempo(1988, 11, 9, 0, 0, 0)
    return {"mensaje": tiempo_IPCC}


@app.get("/nacimiento_convencion")
def covencion():
    tiempo_nacimiento_convencion = calcular_tiempo(1992, 5, 9, 0, 0, 0)
    return {"mensaje": tiempo_nacimiento_convencion}


@app.get("/firma-kioto")
def protocolo_kioto():
    tiempo_kioto = calcular_tiempo(1997, 12, 11, 0, 0, 0)
    return {"mensaje": tiempo_kioto}


@app.get("/acuerdo-paris")
def paris():
    tiempo_acuerdo = calcular_tiempo(2015, 12, 12, 0, 0, 0)
    return {"mensaje": tiempo_acuerdo}


@app.get("/energia-renovable")
def impulso_energia_renovable():
    tiempo_energia = calcular_tiempo(2010, 1, 1, 0, 0, 0)
    return {"mensaje": tiempo_energia}


@app.get("/precio-bajo")
def bateria_precio():
    tiempo_precio = calcular_tiempo(2016, 1, 1, 0, 0, 0)
    return {"mensaje": tiempo_precio}


@app.get("/muralla")
def muralla_verde():
    tiempo_muralla = calcular_tiempo(2007, 1, 29, 0, 0, 0)
    return {"mensaje": tiempo_muralla}
