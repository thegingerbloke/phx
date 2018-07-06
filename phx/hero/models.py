from django.db import models


class Hero(models.Model):
    caption = models.CharField(max_length=200, blank=True)
    image = models.ImageField(
        upload_to='hero/',
        help_text=(
            'Hero images should be at least 1200 pixels wide, '
            'with an aspect ratio of at least 16:9.'
        )
    )

    def __str__(self):
        return self.caption
