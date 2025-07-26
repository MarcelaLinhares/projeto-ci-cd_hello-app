from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Nova mensagem! Deploy automatizado com sucesso!"}