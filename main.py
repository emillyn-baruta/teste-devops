from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/testandodenovo")
async def funcaoteste():
    return {"teste": "tentando testar endpoint"}