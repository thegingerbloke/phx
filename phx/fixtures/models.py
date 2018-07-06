from django.db import models


class Fixtures(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    categories = models.ManyToManyField('Categories', blank=True)
    link_url = models.URLField(max_length=200)

    # Metadata
    class Meta:
        verbose_name = 'Fixture'
        verbose_name_plural = 'Fixtures'

    def __str__(self):
        return self.title


class Categories(models.Model):
    title = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=12)
    icon = models.ImageField(
        upload_to='fixtures/categories/',
        blank=True
    )

    # Metadata
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
