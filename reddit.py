#!/usr/bin/env python

# This is a python script for calling Reddit API



import praw


def reddit():
    
    
    # open a readdit account ,get necessary authorization
    with open('reddit_file.txt', 'r') as f:
        user_id = f.readline().rstrip()
        secret = f.readline().rstrip()
        agent = f.readline().rstrip()
        username = f.readline().rstrip()
        password = f.readline().rstrip()
    f.close()
    

    reddit = praw.Reddit(client_id= user_id,
                     client_secret= secret,
                     user_agent= agent,
                     username= username,
                     password= password)
    
    # string array to store something
    
    
    title = []
    score = []
    id = []
    # get pricture from the webpage that url point to
    url = []
    # content contains everything your need 
    content = [title,score,id,url]
    
    
    subreddit = reddit.subreddit('technology')
    # assume you have a Subreddit instance bound to variable `technology`
    for submission in subreddit.hot(limit=10):
        title.append(submission.title)  # Output: the submission's title
        score.append(submission.score)  # Output: the submission's score
        id.append(submission.id)     # Output: the submission's ID
        url.append(submission.url)    # Output: the URL the submission points to
                                 # or the submission's URL if it's a self post
    return content

    
