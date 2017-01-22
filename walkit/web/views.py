from django.shortcuts import render


from .models import Subreddit


def index(request):
    subreddits = Subreddit.objects.values()
    return render(request, 'web/index.html', context={'subreddits': subreddits})
