from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import strip_tags

from gallery.models import Gallery


class Content(models.Model):
    title = models.CharField(max_length=32)
    gallery = models.ForeignKey(
        Gallery,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    join = RichTextField(config_name='text')
    about = RichTextField(config_name='text')

    class Meta:
        verbose_name = 'home page content'
        verbose_name_plural = 'home page content'

    def __str__(self):
        return 'home page content'


class Announcement(models.Model):
    announcement = RichTextField(config_name='text')
    display_until = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return strip_tags(self.announcement)


class Hero(models.Model):
    image = models.ImageField(
        upload_to='home/hero/',
        help_text=('Hero images should be at least 1200 pixels wide, '
                   'with an aspect ratio of at least 16:9.'))
    caption = models.CharField(max_length=200, blank=True)
    image_categories = models.ManyToManyField('HeroImageCategory', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.caption


class HeroImageCategory(models.Model):
    category = models.CharField(max_length=30)
    count = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'hero image categories'

    def __str__(self):
        return self.category
