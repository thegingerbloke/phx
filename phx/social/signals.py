from django.urls import reverse
from django.conf import settings


def save_news(sender, instance, created, **kwargs):
    if created:
        url = get_news_url(instance)
        save('News', instance.title, url)


def save_results(sender, instance, created, **kwargs):
    if created:
        url = get_results_url(instance)
        save('Results', instance.fixture.title, url)


def save(model, title, url):
    from .models import Social
    social = Social(model=model, title=title, url=url)
    social.save()
    social.post()


def get_news_url(obj):
    url = reverse('news-detail', kwargs={'pk': obj.id, 'slug': obj.slug})
    return '{0}{1}'.format(settings.HOST, url)


def get_results_url(obj):
    url = reverse('results-index')
    return '{0}{1}'.format(settings.HOST, url)
