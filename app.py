from fastapi import FastAPI
from pydantic import BaseModel

#Set this as an API endpoint via FastAPI

app = FastAPI()

class Query(BaseModel):
    texto: str

@app.post("/")
async def insertar_query(query: Query):
    frase_completa = f"Hola, {query.texto}"
    return {"frase_resultante": frase_completa}
