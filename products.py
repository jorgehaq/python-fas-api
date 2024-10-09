from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def root():
    return "Hola Fast Apiz"


@app.get('/products/')
async def products():
    return [
        "Producto 1",
        "Producto 2",
        "Producto 3",
        "Producto 4",
        "Producto 5",
        "Producto 6",
        "Producto 7"
            ]