from django.db import models


ALIGNMENT_CHOICES = (
    ('imageLeft', 'Image left'),
    ('imageRight', 'Image right'),
    ('centre', 'Centre'),
)

BACKGROUND_CHOICES = (
    ('light', 'Light'),
    ('dark', 'Dark'),
    ('white', 'White'),
)


class AbstractComponents(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractEditorials(AbstractComponents):
    content = models.TextField()

    class Meta:
        abstract = True
        verbose_name = 'editorial'
        verbose_name_plural = 'editorials'

    def __str__(self):
        return 'Editorial'


class AbstractFeatures(AbstractComponents):
    # add image field directly where used:
    # image = models.ImageField(upload_to=get_upload_path, blank=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    image_alt = models.CharField(max_length=200, blank=True)
    link_url = models.URLField(max_length=200, blank=True)
    link_text = models.CharField(max_length=200, blank=True)
    align = models.CharField(
      choices=ALIGNMENT_CHOICES,
      max_length=200
    )
    background = models.CharField(
      choices=BACKGROUND_CHOICES,
      max_length=200
    )

    class Meta:
        abstract = True
        verbose_name = 'feature'
        verbose_name_plural = 'features'

    def __str__(self):
        return 'Feature'


class AbstractListItems(AbstractComponents):
    # add image fields directly where used:
    # image_1 = models.ImageField(upload_to=get_upload_path, blank=True)
    # image_2 = models.ImageField(upload_to=get_upload_path, blank=True)
    # image_3 = models.ImageField(upload_to=get_upload_path, blank=True)
    title_1 = models.CharField(max_length=200, blank=True)
    content_1 = models.TextField(blank=True)
    image_alt_1 = models.CharField(max_length=200, blank=True)
    link_url_1 = models.URLField(max_length=200, blank=True)
    link_text_1 = models.CharField(max_length=200, blank=True)
    title_2 = models.CharField(max_length=200, blank=True)
    content_2 = models.TextField(blank=True)
    image_alt_2 = models.CharField(max_length=200, blank=True)
    link_url_2 = models.URLField(max_length=200, blank=True)
    link_text_2 = models.CharField(max_length=200, blank=True)
    title_3 = models.CharField(max_length=200, blank=True)
    content_3 = models.TextField(blank=True)
    image_alt_3 = models.CharField(max_length=200, blank=True)
    link_url_3 = models.URLField(max_length=200, blank=True)
    link_text_3 = models.CharField(max_length=200, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'list item'
        verbose_name_plural = 'list items'

    def __str__(self):
        return 'ListItems'


class AbstractQuotes(AbstractComponents):
    # add image field directly where used:
    # image = models.ImageField(upload_to=get_upload_path, blank=True)
    quote = models.TextField()
    author = models.CharField(max_length=200, blank=True)
    image_alt = models.CharField(max_length=200, blank=True)
    align = models.CharField(
      choices=ALIGNMENT_CHOICES,
      max_length=200
    )
    background = models.CharField(
      choices=BACKGROUND_CHOICES,
      max_length=200
    )

    class Meta:
        verbose_name = 'quote'
        verbose_name_plural = 'quotes'
        abstract = True

    def __str__(self):
        return 'Quote'


class AbstractImages(AbstractComponents):
    # add image field directly where used:
    # image = models.ImageField(upload_to=get_upload_path)
    image_alt = models.CharField(max_length=200, blank=True)
    caption = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
        abstract = True

    def __str__(self):
        return 'Image'
