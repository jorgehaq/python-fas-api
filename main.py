from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return "Hola Fast Api"

@app.get('/url')
async def root():
    return {
        "un curso":"fas api tutorial"
    }