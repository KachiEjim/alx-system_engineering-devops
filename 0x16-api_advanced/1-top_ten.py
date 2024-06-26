#!/usr/bin/python3
""" FILE DOC """

from requests import get


def top_ten(subreddit):
    """
    Prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"

    headers = {"user-agent": "my-app/0.0.1"}

    response = get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        print(None)
        return None

    try:
        result = response.json()

    except ValueError:
        print(None)
        return None

    try:

        data = result.get("data")
        children = data.get("children")
        for child in children[:10]:
            post = child.get("data")
            print(post.get("title"))

    except:
        print(None)
