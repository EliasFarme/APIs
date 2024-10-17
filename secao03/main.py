from fastapi import FastAPI



app = FastAPI

@app.get('/')
async def raiz():
    return{"msg": "Primeira API com FastAPI"}

if __name__ = "__main__":
    uvicorn.run("main:app", host="127.0.0.1", porta=8000, log_level="info", reload=True)