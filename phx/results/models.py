from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

from fixtures.models import Fixture


class Result(models.Model):
    fixture = models.OneToOneField(
        Fixture,
        on_delete=models.CASCADE,
        related_name='fixture',
    )
    results_url = models.URLField(max_length=200, blank=True)
    summary = RichTextField(
        config_name='text',
        blank=True,
        help_text='This is displayed above the results',
    )
    results = RichTextField(config_name='table', )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{0} ({1})'.format(self.fixture.title, self.fixture.event_date)
