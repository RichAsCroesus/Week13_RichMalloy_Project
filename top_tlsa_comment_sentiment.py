
import secrets
import random

from typing import Dict, List

from praw import Reddit
from praw.models.reddit.subreddit import Subreddit
from praw.models import MoreComments

from transformers import pipeline


def get_subreddit(display_name:str) -> Subreddit:
    """Get subreddit object from display name

    Args:
        display_name (str): [description]

    Returns:
        Subreddit: [description]
    """
    REDDIT_API_CLIENT_ID="IXXyy-gM-UCb13XJRUjTBg"
    REDDIT_API_CLIENT_SECRET="GUEsvVEG5AqoRvisBJGxjFgj0SRhSg"
    REDDIT_API_USER_AGENT="FooBar"
    reddit = Reddit(
        client_id=REDDIT_API_CLIENT_ID,        
        client_secret=REDDIT_API_CLIENT_SECRET,
        user_agent=REDDIT_API_USER_AGENT
        )
    
    subreddit = reddit.subreddit("TSLA")
    return subreddit

def get_comments(subreddit:Subreddit, limit:int=3) -> List[str]:
    """ Get comments from subreddit

    Args:
        subreddit (Subreddit): [description]
        limit (int, optional): [description]. Defaults to 3.

    Returns:
        List[str]: List of comments
    """
    top_comments = []
    for submission in subreddit.top(limit=limit):
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            top_comments.append(top_level_comment.body)
    return top_comments

def run_sentiment_analysis(comment:str) -> Dict:
    """Run sentiment analysis on comment using default distilbert model
    
    Args:
        comment (str): [description]
        
    Returns:
        str: Sentiment analysis result
    """
    sentiment_model = pipeline("sentiment-analysis")
    sentiment = sentiment_model(comment)
    return sentiment[0]


if __name__ == '__main__':
    submission = get_subreddit("foo")
    comments = get_comments(submission)
    comment = comments[0]
    sentiment = run_sentiment_analysis(comment)
    
    print(f'The comment: {comment}')
    print(f'Predicted Label is {sentiment["label"]} and the score is {sentiment["score"]:.3f}')
