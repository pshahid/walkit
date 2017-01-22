from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from web.models import Subreddit


class SubredditResource(ModelResource):
    class Meta:
        queryset = Subreddit.objects.all()
        resource_name = 'subreddit'
        authorization = Authorization()