#!/usr/bin/python3
"""
using reddit API
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    The `recurse` function retrieves the titles of the
    hot posts from a given subreddit using the Reddit
    API, and returns them as a list.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {
        'User-Agent': 'Python_Advanced_API_tasks'
    }
    url = F"https://www.reddit.com/r/{subreddit}/hot.json"
    with requests.get(url, headers=headers,
                      params={'after': after}) as response:
        if response.status_code >= 400:
            print(None)
            return
        after = response.json()['data']['after']
        posts = response.json()["data"]["children"]
        if posts is None or posts[0]['kind'] != 't3':
            if hot_list == []:
                return None
            return hot_list
        for post in posts:
            hot_list.append(post['data']['title'])
        if after is None:
            if hot_list == []:
                return None
            return hot_list
        return recurse(subreddit, hot_list, after)
