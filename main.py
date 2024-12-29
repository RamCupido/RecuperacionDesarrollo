from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Formulario(BaseModel):
    sistemas_informacion: str
    ley_benford: str
    tecnologias_nlp: str
    caracteristicas_big_data: str
    datos_enriquecidos: str
    surface_web: str
    embeddings_nlp: str
    reto_heterogeneidad: str
    metodologia_crisp_dm: str
    guardar_csv: str

@app.post("/formulario")
def enviar_formulario(formulario: Formulario):
    #Respuestas Correctas para hacer la comparacion
    respuestas_correctas = {
        "sistemas_informacion": "Son el motor del negocio, pues las nuevas ideas se materializan con tecnología",
        "ley_benford": "Existe una mayor probabilidad de que los primeros números sean el primer dígito",
        "tecnologias_nlp": "Embeddings",
        "caracteristicas_big_data": "Velocidad, Volumen y Variedad",
        "datos_enriquecidos": "Valor y Veracidad",
        "surface_web": "Incluye redes sociales, sitios web y foros accesibles por navegadores convencionales, además de ser indexada por motores de búsqueda",
        "embeddings_nlp": "Son representaciones vectoriales de palabras que permiten a los modelos de NLP avanzados tener una coherencia en sus respuestas",
        "reto_heterogeneidad": "Con la implementación de microservicios que permitan conectar servicios de diferentes tipos",
        "metodologia_crisp_dm": "Entender la lógica de negocio",
        "guardar_csv": "df.to_csv",
    }

    #Pequeña Explicacion de las respuestas correctas
    explicaciones = {
        "sistemas_informacion": "Las ideas tecnológicas impulsan el negocio, ya que en la actualidaad los sistemas de informacion nos permiten usar la tecnologia para buscar soluciones",
        "ley_benford": "La Ley de Benford se basa en la probabilidad de que ciertos números aparezcan más como primer dígito, es decir que hay mas probabilidad de que un número comience con el 1 que con el 9",
        "tecnologias_nlp": "Embeddings es una librería popular para NLP avanzado, la cual se usa en GPT y BERT",
        "caracteristicas_big_data": "Las características clave del Big Data son velocidad (Por el tiempo de respuesta), volumen (Por las grandes candidades de datos) y variedad (Por los diferecntes tipos de datos que puede tener)",
        "datos_enriquecidos": "El enriquecimiento de datos los damos nosotros después de pasar por un 'Filtro' y este agrega valor y mejora la veracidad,",
        "surface_web": "La Surface Web incluye sitios accesibles e indexados por motores de búsqueda, mediante aplicaciones comunes que nostros usamos en nuestro día a día como Google, Opera, Moxilla, etc..",
        "embeddings_nlp": "Los embeddings son representaciones vectoriales que dan coherencia en NLP",
        "reto_heterogeneidad": "Los microservicios permiten manejar la heterogeneidad en sistemas distribuidos, ayudandonos a dividir nuestro aplicacion en pequeños servicios para poder usar diferentes tecnologias o tener diferentes propositos",
        "metodologia_crisp_dm": "Entender la lógica de negocio es el primer paso clave en CRISP-DM",
        "guardar_csv": "La función 'Df.to_csv' guarda datos de un DataFrame en formato CSV",
    }

    # Comparar las respuestas enviadas con las correctas
    resultados = []
    for pregunta, respuesta_correcta in respuestas_correctas.items():
        respuesta_usuario = getattr(formulario, pregunta)
        es_correcto = respuesta_usuario == respuesta_correcta
        resultados.append({
            "pregunta": pregunta,
            "respuesta_usuario": respuesta_usuario,
            "respuesta_correcta": respuesta_correcta,
            "es_correcto": es_correcto,
            "explicacion": explicaciones[pregunta],
        })

    return {
        "mensaje": "Formulario evaluado exitosamente",
        "resultados": resultados,
    }


@app.get("/", response_class=HTMLResponse)
def servir_frontend():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

