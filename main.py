from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/lazio")
async def uhuy():
    return {"msg": "Petronazz"}