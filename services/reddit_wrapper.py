import praw
import os

def __get_reddit_client():
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=os.getenv("USER_AGENT"),
    )
    return reddit


def get_comments():
    reddit = __get_reddit_client()
    subreddit = reddit.subreddit('AskReddit')
    submissions = subreddit.hot(limit=1)

    for submission in submissions:
        submission.comments.replace_more(limit=0)
        comments = [comment.body_html for comment in submission.comments[:5]]
        return {
            "title": submission.title,
            "body": submission.selftext,
            "comments": comments,
            "url": submission.url,
        }
    return None
