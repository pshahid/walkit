from django.db import models


class Subreddit(models.Model):
    name = models.CharField(max_length=25)
    created_date = models.DateTimeField()
    subscribers = models.IntegerField()


class SubredditLink(models.Model):  # A self-referential MxM through model; TODO later
    pass
