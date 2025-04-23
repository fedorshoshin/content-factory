from fastapi import FastAPI
from clients import praw_client
import main

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/conv")
def get_conversation():
    return main.make_conversation_short()
@app.get("/comments")

def get_comments():
    return praw_client.get_comments()