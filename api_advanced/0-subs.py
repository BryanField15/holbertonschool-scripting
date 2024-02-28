#!/usr/bin/python3

"""
This module queries the Reddit API to return the number of subscribers for a given subreddit.
If the subreddit is invalid or does not exist, it returns 0.
"""

import requests


def number_of_subscribers(subreddit):
  '''
    Returns the number of subscribers for a subreddit.

    Args:
    subreddit (str): The subreddit name to query.

    Returns:
    int: The number of subscribers if the subreddit exists, otherwise 0.
    '''
  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {'User-Agent': 'APIAdvanced/0.1 (Educational Purpose; Student at Holberton)'}

  response  = requests.get(url, headers=headers)
  if response.status_code == 200:
    body = response.json()

    if 'data' in body:
      body_data = body['data']

      if 'subscribers' in body_data:
        return body_data['subscribers']
      else:
        return 0
    else:
      return 0
  else:
    return 0
