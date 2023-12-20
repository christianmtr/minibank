from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    """Index endoint"""
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
