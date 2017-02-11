""" Any Requestor in this file is an adapter that conforms to the IReddit interface. This makes it
easier to plug in different APIs or our own custom APIs as we see fit.

At the moment we use PRAW as the context to make requests from, because we don't want to violate
Reddit's Terms of Use. However, if we find later that simply requesting the about.json endpoints
is not bound by the TOU or authentication rules, then we can flip over to unauthenticated requests
to get a higher throughput of data.

IReddit should be considered an internal API, so it can break at will.
"""


class IReddit(object):

    def __init__(self, context=None):
        self.context = context

    def about(self, name):
        """ Return about.json for a single subreddit """

    def defaults(self):
        """ Return a list of subreddits which are the 'defaults' for Reddit. """

    def popular(self):
        """ Return a list of subreddits which are the most 'popular' for Reddit """


class AuthenticatedRequestor(IReddit):

    def __init__(self, context=None):
        super().__init__(context=context)

    def about(self, name):
        if not name.startswith('r/'):
            name = 'r/{0}'.format(name)

        url = '{0}/about.json'.format(name)
        # Throws prawcore.exceptions on errors
        return self.context.request('GET', url)

    def defaults(self):
        for d in self.context.subreddits.default():
            yield d.display_name

    def popular(self):
        for p in self.context.subreddits.popular():
            yield p.display_name