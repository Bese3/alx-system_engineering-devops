#!/usr/bin/python3
"""
using the reddit api
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    The function `number_of_subscribers`
    returns the number of subscribers for a given subreddit by
    making a request to the Reddit API.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {
        'User-Agent': 'Python_Advanced_API_tasks'
    }
    url = F"https://www.reddit.com/r/{subreddit}/about.json"
    with requests.get(url, headers=headers) as response:
        return response.json()["data"]["subscribers"]
