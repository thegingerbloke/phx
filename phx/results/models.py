from django.db import models
from fixtures.models import Fixtures
from django.contrib.auth.models import User


class Results(models.Model):
    fixture = models.OneToOneField(
        Fixtures,
        on_delete=models.CASCADE,
        related_name='fixture',
    )
    results_url = models.URLField(max_length=200, blank=True)
    summary = models.TextField(
        blank=True,
        help_text='This is displayed above the results',
    )
    results = models.TextField()
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
        verbose_name = 'Result'
        verbose_name_plural = 'Results'

    def __str__(self):
        return self.fixture.title
