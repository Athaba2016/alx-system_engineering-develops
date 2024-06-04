#!/usr/bin/python3
"""Script queries subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Read reddit API and returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "0x16.api.advance (my_user_ agent._)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
