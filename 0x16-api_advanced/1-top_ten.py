#!/usr/bin/python3
"""
using reddit API
"""
import json
import requests


def top_ten(subreddit):
    """
    The `top_ten` function retrieves the top ten posts from
    a specified subreddit on Reddit and prints
    their titles.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {
        'User-Agent': 'Python_Advanced_API_tasks'
    }
    url = F"https://www.reddit.com/r/{subreddit}/hot.json"
    with requests.get(url, headers=headers, params={'limit': 10}) as response:
        if response.status_code >= 400:
            print(None)
            return
        posts = response.json()["data"]["children"]
        if posts is None or posts[0]['kind'] != 't3':
            print(None)
            return
        for i in posts:
            print(i['data']['title'])
