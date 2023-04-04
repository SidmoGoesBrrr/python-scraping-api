#a basic project which uses fast api to return hello when pinged at hello world
from fastapi import FastAPI
app = FastAPI()

#this is the function which is called when the server is pinged at hello
@app.get("/scrape")
def read_hello():
    return {"Hello": "World"}