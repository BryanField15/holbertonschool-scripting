#!/usr/bin/python3
"""
This module queries the Reddit API, parses the title of all hot articles, 
and prints a sorted count of given keywords (case-insensitive, 
delimited by spaces
"""

import requests

def count_words(subreddit, word_list, after='', word_count={}):
    """
    Recursively counts and prints the occurrences of keywords in the titles
    of hot articles for a given subreddit.

    Args:
    subreddit (str): The subreddit to search.
    word_list (list): A list of keywords to search for.
    after (str, optional): The pagination parameter for Reddit's API.
    word_count (dict, optional): Accumulates the count of each keyword.
    """
    # Prepare the request
    headers = {
    'User-Agent': 'python:edu.holberton.apiadvanced:v1.0.0 (by /u/MintyGreen15)'
    } 
    url = (
    f"https://www.reddit.com/r/{subreddit}/hot.json"
    f"?limit=100&after={after}"
    )
    response = requests.get(url, headers=headers)

    # Base case: if the subreddit is invalid or we've reached the end
    if response.status_code != 200 or after is None:
        if after is None:  # Only print the results after all pages have been processed
            if word_count:
                sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    print(f"{word}: {count}")
            return
        else:
            return

    # Process the response
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    after = data.get('data', {}).get('after')

    # Initialize word_count dict on first call
    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}

    # Count occurrences of each word in the current batch of post titles
    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] += title.split().count(word_lower)

    # Recursively process the next batch of posts
    count_words(subreddit, word_list, after, word_count)