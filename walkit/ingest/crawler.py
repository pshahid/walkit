""" Specifically for subreddit discovery, this module is intended to find new subreddits by finding
new ones in different ways: sidebar, moderated-by, mentioned-in, etc.
"""

import requests
import json
import re
from datetime import datetime
from collections import defaultdict

from prawcore.exceptions import BadRequest, Redirect, NotFound, Forbidden


class VisitorError(Exception):
    pass


def crawled(reddit):
    """ Begin crawling the entire site starting from defaults """
    for default in reddit.subreddits.default():
        for results in bfs(default.display_name, reddit):
            yield results


def visit(name, reddit):
    """ Visit a subreddit and return data or raise an error """

    print(name)
    try:
        about = reddit.request('GET', 'r/{0}/about.json'.format(name))
    except (BadRequest, Redirect, Forbidden) as e:
        raise VisitorError from e
    except NotFound as e:
        print("Subreddit not found {0}".format(name))
        raise VisitorError from e
    else:
        description_str = str(about['data']['description'].encode('ascii', 'ignore'))
        related = set([s.lstrip('r/') for s in re.findall('r\/\w+', description_str)])

    stats = {
        'related': related,
        'name': name,
        'subscribers': about['data']['subscribers'],
        'created': str(datetime.fromtimestamp(about['data']['created'])),
        'public_description': about['data']['public_description'],
        'description': description_str
    }

    return stats


def duplicate_finder():
    """ Prints to stdout when it finds a duplicate in the queue """
    while True:
        queue = yield
        queue_set = set(queue)
        try:
            assert len(queue) == len(queue_set)
        except AssertionError:
            print("Duplicates found in queue: ")
            found = set()
            duplicates = defaultdict(int)
            for i in queue:
                if i in found:
                    duplicates[i] += 1
                else:
                    found.add(i)
            print(duplicates)


def bfs(start, reddit):
    """ BFS which accepts a start name and visits until it empties the queue"""
    # Use a list as a queue
    dupe_finder = duplicate_finder()
    next(dupe_finder)
    queue = [start]
    visited = set()

    while queue:
        dupe_finder.send(queue)
        subreddit = queue.pop(0)
        try:
            results = visit(subreddit, reddit)
        except VisitorError as ve:
            print("Got VisitorError while visiting {0}".format(subreddit))
        else:
            visited.add(subreddit)
            related_set = set(results['related'])
            # Extend queue by what is related, not visited and not in the queue
            queue += list(related_set - visited - set(queue))

        yield results
