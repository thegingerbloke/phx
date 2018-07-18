from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from hero.models import Hero
from components.models import (AbstractEditorial, AbstractFeature,
                               AbstractQuote, AbstractImage,
                               AbstractListItems)


def generate_slug(instance):
    if instance.parent:
        return '{0}{1}/'.format(instance.parent.slug, slugify(instance.title))
    else:
        return '/{0}/'.format(slugify(instance.title))


class Page(models.Model):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    slug = AutoSlugField(
        help_text='This will be the URL for this page',
        unique=True,
        overwrite=True,
        slugify_function=lambda value: value,
        populate_from=generate_slug
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    hero = models.ForeignKey(
        Hero,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    # Metadata
    class Meta:
        ordering = ['created_date']

    # Methods
    def get_absolute_url(self):
        return reverse('page-detail', args=[self.slug])

    def __str__(self):
        return self.title


class Component(models.Model):
    order = models.IntegerField(
        blank=True,
        null=True,
    )
    page = models.ForeignKey(
        Page,
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
        id = self.component.page_id
        return 'page/{0}/features/{1}'.format(id, filename)

    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='feature',
    )
    image = models.ImageField(upload_to=get_upload_path, blank=True)


class Quote(AbstractQuote):
    def get_upload_path(self, filename):
        id = self.component.page_id
        return 'page/{0}/quotes/{1}'.format(id, filename)

    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='quote',
    )
    image = models.ImageField(upload_to=get_upload_path, blank=True)


class Image(AbstractImage):
    def get_upload_path(self, filename):
        id = self.component.page_id
        return 'page/{0}/images/{1}'.format(id, filename)

    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='image',
    )
    image = models.ImageField(upload_to=get_upload_path)


class ListItems(AbstractListItems):
    help_text = 'Image will be cropped and resized to 800x400'

    def get_upload_path(self, filename):
        id = self.component.page_id
        return 'page/{0}/list-items/{1}'.format(id, filename)

    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='list_items',
    )
    image_1 = models.ImageField(
        upload_to=get_upload_path,
        blank=True,
        help_text=help_text
    )
    image_2 = models.ImageField(
        upload_to=get_upload_path,
        blank=True,
        help_text=help_text
    )
    image_3 = models.ImageField(
        upload_to=get_upload_path,
        blank=True,
        help_text=help_text
    )
