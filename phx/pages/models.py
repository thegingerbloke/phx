from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
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
        help_text=(
            'Select section of the site this page should appear in, '
            'leave blank if this page shouldn\'t appear under any section'
        )
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
        return reverse('page-detail', kwargs={
            'slug': self.get_slug()
        })

    # strip tags from slug before returning
    def get_slug(self):
        return self.slug.lstrip('/').rstrip('/')

    # disallow selecting self as parent
    def clean(self):
        if self.parent == self:
            raise ValidationError("A page can't be its own parent")

    # display parent hierarchy in admin dropdown list
    def __str__(self):
        hierarchy = []
        self.generate_hierarchy(self, hierarchy)
        title = ' ↣ '.join(hierarchy)
        return title

    def generate_hierarchy(self, instance, hierarchy):
        hierarchy.insert(0, instance.title)
        if instance.parent:
            self.generate_hierarchy(instance.parent, hierarchy)


class Component(models.Model):
    order = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name='components',
    )

    # Metadata
    class Meta:
        ordering = ['order']

    def __str__(self):
        return '#{0}'.format(self.order + 1)


class Editorial(AbstractEditorial):
    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='editorial',
    )


class Feature(AbstractFeature):
    def get_upload_path(self, filename):
        id = self.component.page_id
        return 'page/{0}/feature/{1}'.format(id, filename)

    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='feature',
    )
    image = models.ImageField(upload_to=get_upload_path, blank=True)


class Quote(AbstractQuote):
    def get_upload_path(self, filename):
        id = self.component.page_id
        return 'page/{0}/quote/{1}'.format(id, filename)

    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE,
        related_name='quote',
    )
    image = models.ImageField(upload_to=get_upload_path, blank=True)


class Image(AbstractImage):
    def get_upload_path(self, filename):
        id = self.component.page_id
        return 'page/{0}/image/{1}'.format(id, filename)

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
