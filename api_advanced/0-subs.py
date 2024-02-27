#!/usr/bin/python3

'''Function queries Reddit API and returns number of subscribers'''
import requests


def number_of_subscribers(subreddit):
  '''Returns the number of subscribers for a subreddit'''
  url = f"https://www.reddit.com/r/{subreddit}/about.json"

  response  = requests.get(url)
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
