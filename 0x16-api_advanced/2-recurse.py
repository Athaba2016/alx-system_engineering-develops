#!/usr/bin/python3
"""
Using reddit's API
"""
import requests

def recurse(subreddit):
    """returning top ten post titles recursively"""
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 404:
        return []
    elif results.status_code == 200:
        all_titles = []
        after_data = None
        while True:
            all_titles.extend([title.get("data").get("title") for title in results.json().get("data").get("children")])
            after_data = results.json().get("data").get("after")
            if after_data is None:
                break
            results = requests.get(url, params={'after': after_data}, headers=user_agent,
                                   allow_redirects=False)
        return all_titles
    else:
        return []
