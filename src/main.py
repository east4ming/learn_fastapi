from fastapi import FastAPI

app = FastAPI()

# First Steps
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Path Parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Path Parameters: Order
@app.get("/users/me")
async def read_user_me():
    return {"users_me": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
