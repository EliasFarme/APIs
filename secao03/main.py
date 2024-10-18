from fastapi import FastAPI



app = FastAPI

curso = {
    "Titulo": "Programação para iniciantes"
    "aulas": 114,
    "horas": 58
    }
    2: {
        "Titulo": "APi em python"
        "Aulas": 12,
        "Horas": 30

    } 

@app.get('/aprendizado')
async def get_aprendizado():
    return aprendizado




if __name__ = "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", porta=8000, log_level="info", reload=True)