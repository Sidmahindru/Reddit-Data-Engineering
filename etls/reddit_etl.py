import sys
import numpy as np
import pandas as pd
import praw
from praw import Reddit

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)
        print("connected to reddit!")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)


def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)
    
    dict = {"id":[],
            "title":[],
            "score":[],
            "num_comments":[],
            "author":[],  
            "created_utc":[], 
            "url": [], 
            "over_18": []}
    
    for post in posts:
        #print(post.id)
        #print(post.title)
        #print(post.score)
        #print(post.num_comments)
        #print(post.author)
        #print(post.created_utc)
        #print(post.url)
        #print(post.over_18)
        
        dict["id"].append(post.id)
        dict["title"].append(post.title)
        dict["score"].append(post.score)
        dict["num_comments"].append(post.num_comments)
        dict["author"].append(post.author)
        dict["created_utc"].append(post.created_utc)
        dict["url"].append(post.url)
        dict["over_18"].append(post.over_18)

    post_df = pd.DataFrame(dict)
    return post_df


def transform_data(post_df: pd.DataFrame):
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False)
    post_df['author'] = post_df['author'].astype(str)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['title'] = post_df['title'].astype(str)

    return post_df


def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)