from clients import praw_client
import data_converter


def make_conversation_short():
    response = praw_client.get_comments()
    texts = data_converter.string_to_txt("conversation", response['comments'])
    result = []
    for text in texts:
        result.append(open(text, "r", encoding="utf-8").read())

    return {
        "url": response['url'],
        "title": response['title'],
        "comments": result
    }
