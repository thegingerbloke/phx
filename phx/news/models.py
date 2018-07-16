from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User
from django.urls import reverse
from components.models import (AbstractEditorial, AbstractFeature,
                               AbstractQuote, AbstractImage,
                               AbstractListItems)


class News(models.Model):
    """ News articles """

    # Fields
    title = models.CharField(max_length=200)
    slug = AutoSlugField(
        populate_from='title',
        help_text='This is used as the URL for this news item',
        unique=True
    )
    summary = models.TextField(
        max_length=1000,
        help_text='This is the text used as the description of the article',
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    # Metadata
    class Meta:
        verbose_name = 'news article'
        verbose_name_plural = 'news articles'
        ordering = ['-created_date']

    # Methods
    def get_absolute_url(self):
        return reverse('news-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.title


class Thumbnail(models.Model):
    def get_upload_path(self, filename):
        id = self.news_id
        return 'news/{0}/thumbnail/{1}'.format(id, filename)

    news = models.OneToOneField(
        News,
        on_delete=models.CASCADE,
        related_name='thumbnail',
    )
    image = models.ImageField(upload_to=get_upload_path, blank=True)
    image_alt = models.CharField(max_length=200, blank=True)


class Component(models.Model):
    order = models.IntegerField(
        blank=True,
        null=True,
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='components',
    )

    # Metadata
    class Meta:
        ordering = ['order']


class Editorial(AbstractEditorial):
    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='editorial',
    )


class Feature(AbstractFeature):
    def get_upload_path(self, filename):
        id = self.component.news_id
        return 'news/{0}/features/{1}'.format(id, filename)

    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='feature',
    )
    image = models.ImageField(upload_to=get_upload_path, blank=True)


class Quote(AbstractQuote):
    def get_upload_path(self, filename):
        id = self.component.news_id
        return 'news/{0}/quotes/{1}'.format(id, filename)

    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='quote',
    )
    image = models.ImageField(upload_to=get_upload_path, blank=True)


class Image(AbstractImage):
    def get_upload_path(self, filename):
        id = self.component.news_id
        return 'news/{0}/images/{1}'.format(id, filename)

    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='image',
    )
    image = models.ImageField(upload_to=get_upload_path)


class ListItems(AbstractListItems):
    def get_upload_path(self, filename):
        id = self.component.news_id
        return 'news/{0}/list-items/{1}'.format(id, filename)

    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='list_items',
    )
    image_1 = models.ImageField(upload_to=get_upload_path, blank=True)
    image_2 = models.ImageField(upload_to=get_upload_path, blank=True)
    image_3 = models.ImageField(upload_to=get_upload_path, blank=True)
