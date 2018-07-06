from django.db import models
from fixtures.models import Fixtures


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

    # Metadata
    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Results'

    def __str__(self):
        return self.fixture.title
