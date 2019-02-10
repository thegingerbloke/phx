import facebook
from django.conf import settings
from django.db import models
from twitter import OAuth, Twitter


class Social(models.Model):
    model = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    posted = models.BooleanField(default=False)
    reposted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'social media post'

    def __str__(self):
        return self.title

    def post(self):
        model = Social.objects.filter(
            posted=False).order_by('-created_date')[:1].first()

        if model:
            message = self.create_message(model, 'Latest ')
            self.post_to_twitter(message)
            self.post_to_facebook(message)
            model.posted = True
            model.save()

    def repost(self):
        model = Social.objects.filter(
            reposted=False).order_by('created_date')[:1].first()

        if model:
            message = self.create_message(model)
            self.post_to_twitter(message)
            self.post_to_facebook(message)
            model.reposted = True
            model.save()

    def create_message(self, model, prefix=''):
        return '{0}{1}:\n{2} \n\n{3}'.format(prefix, model.model, model.title,
                                             model.url)

    def post_to_twitter(self, message):
        if hasattr(settings, 'TWITTER'):
            try:
                t = Twitter(
                    auth=OAuth(settings.TWITTER['oauth_token'],
                               settings.TWITTER['oauth_secret'],
                               settings.TWITTER['consumer_key'],
                               settings.TWITTER['consumer_secret']))
                t.statuses.update(status=message)
            except:  # noqa
                # todo - catch twitter errors
                pass

    def post_to_facebook(self, message):
        if hasattr(settings, 'FACEBOOK'):
            try:
                graph = facebook.GraphAPI(
                    access_token=settings.FACEBOOK['access_token'], )
                page_id = settings.FACEBOOK['page_id']
                graph.put_object(page_id, 'feed', message=message)
            except:  # noqa
                # todo - catch facebook errors
                pass
