from fastapi import FastAPI
from services import reddit_wrapper
from services import speech_synthesizer
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
    return reddit_wrapper.get_comments()


@app.get("/tts")
def test_tts():
    print('enter your text')
    text = input()
    speech_synthesizer.text_to_speech(text, "result")
