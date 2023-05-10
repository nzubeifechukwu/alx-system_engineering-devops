#!/usr/bin/python3
'''This module contains a function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit
'''
import requests


def top_ten(subreddit):
    '''Print the first 10 hot posts listed for a given subreddit

    Args:
        subreddit: Given subreddit
    '''
    resp = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.format(
        subreddit), headers={'User-agent': 'Nzube'})

    if resp.status_code == 200:
        for child in resp.json().get('data').get('children'):
            print(child.get('data').get('title'))
    else:
        print(None)
