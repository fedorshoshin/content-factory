from services import reddit_wrapper
from services.data_converter import DataConverter
from services import speech_synthesizer
import os
import dotenv

dotenv.load_dotenv()


def make_conversation_short():
    conversation = reddit_wrapper.get_comments()
    clean_text = DataConverter.clear_html(conversation['comments'])

    speech_synthesizer.text_to_speech(clean_text, "record")


def make_survey_short():
    answers = reddit_wrapper.get_comments()
