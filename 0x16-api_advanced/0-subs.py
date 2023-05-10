#!/usr/bin/python3
'''This module contains a function that queries the Reddit API and returns
    the number of for a given subreddit.
'''
import requests


def number_of_subscribers(subreddit):
    '''Query the Reddit API for the number of subscribers to a subreddit

    Args:
        subreddit: Given subreddit to query its number of subscribers

    Return:
        Number of subscribers to @subreddit or 0 if @subreddit is invalid
    '''
    response = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers={'User-agent': 'Nzube'})

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')

    return 0
