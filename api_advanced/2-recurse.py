#!/usr/bin/python3
"""
Recursively fetches titles of hot posts from a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively collects titles of hot posts from a subreddit.
    
    Args:
    subreddit (str): The subreddit to query.
    hot_list (list): Accumulator for hot post titles, passed recursively.
    after (str): Pagination parameter for the next batch of posts.

    Returns:
    list: A list of titles, or None if the subreddit is invalid.
    """
    headers = {
    'User-Agent': (
        'APIAdvanced/0.1 '
        '(Educational Purpose; Student at Holberton School)'
    )
}

    url = (
    f"https://www.reddit.com/r/{subreddit}/hot.json"
    f"?limit=100&after={after}"
)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            if not hot_list:
                return None
            return hot_list
        for post in posts:
            title = post.get('data', {}).get('title')
            if title:
                hot_list.append('title')
        after = data.get('data', {}).get('after')
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except ValueError:
        return None
    