from django.db import models
from django.contrib.auth.models import User


class Hero(models.Model):
    caption = models.CharField(max_length=200, blank=True)
    image = models.ImageField(
        upload_to='hero/',
        help_text=(
            'Hero images should be at least 1200 pixels wide, '
            'with an aspect ratio of at least 16:9.'
        )
    )
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
