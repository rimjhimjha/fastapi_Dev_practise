from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index() -> dict[str,int]:
    return {'hello':123}

@app.get("/about")
async def about()-> str:
    return 'An exceptional Company.'