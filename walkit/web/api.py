from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.validation import Validation
from tastypie.fields import ManyToManyField, ForeignKey
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from web.models import Subreddit, SubredditLink
from django.db.models import ObjectDoesNotExist


class SubredditExistsValidation(Validation):
    def __init__(self, mandatory_fields=None):
        super(SubredditExistsValidation, self).__init__()

        self.mandatory_fields = mandatory_fields

    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'No data available'}

        print(bundle.data)
        errors = {}

        try:
            queryset = Subreddit.objects.filter(name=bundle.data['name'])
            print(queryset)
            assert len(queryset) == 0
        except KeyError:
            errors['name'] = 'No subreddit name provided.'
        except AssertionError:
            errors['__all__'] = 'Record exists. Use PUT to update.'
        except ObjectDoesNotExist:
            pass

        return errors

class SubredditResource(ModelResource):
    subreddit_links = ManyToManyField('web.api.SubredditLinkResource', 'related_subreddits',
                                      full=True, readonly=True, blank=True, null=True)

    class Meta:
        queryset = Subreddit.objects.all()
        resource_name = 'subreddit'
        authorization = Authorization()
        filtering = {
            'name': ALL_WITH_RELATIONS
        }
        validation = SubredditExistsValidation()



class SubredditLinkResource(ModelResource):
    from_subreddit = ForeignKey('web.api.SubredditResource', 'from_subreddits')
    to_subreddit = ForeignKey('web.api.SubredditResource', 'to_subreddits')

    class Meta:
        queryset = SubredditLink.objects.all()
        resource_name = 'subredditlinks'
        authorization = Authorization()
