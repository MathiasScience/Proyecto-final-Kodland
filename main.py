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
