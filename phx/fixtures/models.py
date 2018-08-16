from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Fixture(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateField()
    age_groups = models.CharField(
        max_length=200,
        blank=True,
        help_text='Comma-separated list, or leave blank for open/senior'
    )
    location = models.CharField(max_length=200, blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    link_url = models.URLField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.event_date)


class Category(models.Model):
    alphanumeric = RegexValidator(
        r'^[0-9a-zA-Z]*$',
        'Only alphanumeric characters (a-z, 0-9) are allowed.'
    )

    title = models.CharField(max_length=50)
    abbreviation = models.CharField(
        max_length=12,
        help_text='Please ensure this doesn\'t contain any spaces',
        validators=[alphanumeric]
    )
    icon = models.ImageField(
        upload_to='fixtures/categories/',
        blank=True
    )

    # Metadata
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
