""" Specifically for subreddit discovery, this module is intended to find new subreddits by finding
new ones in different ways: sidebar, moderated-by, mentioned-in, etc.
"""

import requests
import json
import traceback
import re
from datetime import datetime
from collections import defaultdict

from prawcore.exceptions import BadRequest, Redirect, NotFound, Forbidden

# TODO: Move to utilities
def to_py2bytes(s):
    """ Tries to handle utf-8 unicode coming from """
    if not s:
        return ''
    else:
        try:
            return s.decode('utf-8', 'backslashreplace')
        except:
            return s.encode('ascii', 'backslashreplace')


class VisitorError(Exception):
    pass


class TraversalContext(object):
    """ A traversal context is a place to hold the state for our subreddit traversal. Earlier we had
    named things according to the traversal strategy, e.g. bfs or dfs. Instead, we keep it
    generic so we can swap them out if we want to. It's also useful because the way in which something
    visits is decoupled from the visiting function.

    Note: the only difference between the strategies is technically the insertion position. With
    this knowledge we know we can just make a few utilitarian functions instead of entirely new
    objects.
    """

    def __init__(self, request_fn, strategy='bfs'):
        self.request = request_fn  # Request must impl this interface: fn(str: name)
        self.undiscovered = []
        self.strategy = strategy
        self.discovered = set()

    def _insert_dfs(self, undiscovered):
        if isinstance(undiscovered, str):
            self.undiscovered.append(undiscovered)
        elif isinstance(undiscovered, list):
            self.undiscovered.extend(list)
        else:
            raise TypeError("Cannot add type {0} to undiscovered".format(type(undiscovered)))

    def _insert_bfs(self, undiscovered):
        if isinstance(undiscovered, str):
            self.undiscovered.insert(0, undiscovered)
        elif isinstance(undiscovered, list):
            self.undiscovered = undiscovered + self.undiscovered
        else:
            raise TypeError("Cannot add type {0} to undiscovered".format(type(undiscovered)))

    def _insert_undiscovered(self, undiscovered):
        if self.strategy == 'bfs':
            self._insert_bfs(undiscovered)
        elif self.strategy == 'dfs':
            self._insert_dfs(undiscovered)

    def visit(self, name):
        """ Visit a subreddit by making a request for information, return results """
        try:
            about = self.request(name)
        except (BadRequest, NotFound, Redirect, Forbidden) as e:
            raise VisitorError from e

        description = about['data']['description']
        public_description = about['data']['public_description']
        related = set([s.lstrip('r/') for s in re.findall('r/\w+', description)])
        subreddit = {
            'related': related,
            'name': name,
            'subscribers': about['data']['subscribers'],
            'created': str(datetime.fromtimestamp(about['data']['created'])),
            'public_description': public_description,
            'description': description
        }

        return subreddit

    def traverse(self, start):
        """ Beginning with a name `start`, traverse through the list of subs related to `start` """
        self._insert_undiscovered(start)

        while self.undiscovered:
            try:
                name = self.undiscovered.pop(0)
                subreddit = self.visit(name)
            except VisitorError as e:
                print("VisitorError")
                print(traceback.format_exc())
                continue
            except StopIteration:
                break
            else:
                self.discovered.add(name)
                undiscovered = list(subreddit['related'] - self.discovered)
                self._insert_undiscovered(undiscovered)
                yield subreddit


def crawled(defaults, request):
    """ Begin crawling the entire site starting from a list of defaults, needs a `request` function
    that the TraversalContext can use to a visit a subreddit's information.

    Request function must return a dict conforming to the structure of a subreddit's about page.

    :param iterable defaults: Must be an list-like iterable or generator
    :param function request: Request function for about page, must implement this interface:
    fn(str: name), where `name` is a subreddit name.
    """
    context = TraversalContext(request)
    for default in defaults:
        for results in context.traverse(default):
            yield results


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



