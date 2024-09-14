from fastapi import FastAPI
from pydantic import BaseModel

#Set this as an API endpoint via FastAPI

app = FastAPI()

class Query(BaseModel):
    texto: str

@app.post("/")
def insertar_query(query: Query):
    return {"frase_resultante": f"Hola, {query.texto}"}
