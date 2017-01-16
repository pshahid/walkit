""" Specifically for subreddit discovery, this module is intended to find new subreddits by finding
new ones in different ways: sidebar, moderated-by, mentioned-in, etc.
"""

import requests
import json
import re

from prawcore.exceptions import BadRequest, Redirect, NotFound, Forbidden


class VisitorError(Exception):
    pass


def crawled(reddit):
    """ Begin crawling the entire site starting from defaults """
    for default in reddit.subreddits.default():
        for related in bfs(default.display_name, reddit):
            yield related


def visit(name, reddit):
    """ Visit a subreddit and return data or raise an error """

    try:
        about = reddit.request('GET', 'r/{0}/about.json'.format(name))
        # subreddit = reddit.subreddit(name)
    except BadRequest as e:
        raise VisitorError from e
    except Redirect as e:
        raise VisitorError from e
    except Forbidden as e:
        raise VisitorError from e
    else:
        description_str = about['data']['description']
        related = set([s.strip('r/') for s in re.findall('r\/\w+', description_str)])

    print(name)
    stats = {
        'related': related
        # 'traffic': subreddit.traffic()
    }

    return stats


def bfs(start, reddit):
    """ BFS which accepts a start name and visits until it empties the queue"""
    # Use a list as a queue
    queue = [start]
    visited = set()

    while queue:
        subreddit = queue.pop(0)
        try:
            results = visit(subreddit, reddit)
        except VisitorError as ve:
            print("Got VisitorError while visiting {0}".format(subreddit))
        else:
            visited.add(subreddit)

            for related in results['related']:
                if related not in visited:
                    queue.append(related)

        yield subreddit
