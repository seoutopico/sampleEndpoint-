from fastapi import FastAPI

app = FastAPI()

@app.get("/saludo")
async def saludo(query: str):
    return {"mensaje": f"Hola, {query}"}

