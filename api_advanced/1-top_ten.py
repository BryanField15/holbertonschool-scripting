#!/usr/bin/python3

"""
This module queries the Reddit API prints the titles of the first 10 hot posts listed for a given subreddit.
If the subreddit is invalid or does not exist, it prints None.
"""

import requests


def top_ten(subreddit):
  '''
    Returns the number of subscribers for a subreddit.

    Args:
    subreddit (str): The subreddit name to query.

    Returns:
    None: Prints titles of the top ten hot posts or None if subreddit is invalid.
    '''
  
  url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
  headers = {'User-Agent': 'APIAdvanced/0.1 (Educational Purpose; Student at Holberton)'}
  r  = requests.get(url, headers=headers, allow_redirects=False)
  
  if r.status_code != 200:
    print(None)
    return

  try:
    top_ten = r.json().get('data').get('children')
    for post in top_ten:
      print(post.get('data').get('title'))
  except ValueError:
    print(None)