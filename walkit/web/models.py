from django.db import models
from datetime import datetime, MINYEAR


class Subreddit(models.Model):
    name = models.CharField(max_length=25, unique=True)
    public_description = models.TextField(max_length=1024, blank=True)
    sidebar_description = models.TextField(blank=True)
    created_date = models.DateTimeField()
    subscribers = models.IntegerField()
    last_updated_date = models.DateTimeField(null=True, default=datetime(MINYEAR, 1, 1))
    subreddit_links = models.ManyToManyField('self',
                                             related_name='related_subreddits+',
                                             through='SubredditLink',
                                             symmetrical=False,
                                             blank=True)


class SubredditLink(models.Model):  # A self-referential MxM through model; TODO later
    from_subreddit = models.ForeignKey(Subreddit, related_name='from_subreddits')
    to_subreddit = models.ForeignKey(Subreddit, related_name='to_subreddits')
