from django.db import models


class Contact(models.Model):
    name = models.CharField(
        max_length=200,
        help_text=('This is won\'t be displayed on the site but helps us '
                   'to identify contacts'),
    )
    email = models.EmailField(
        max_length=200,
        help_text=('This is won\'t be displayed on the site but helps us '
                   'to identify contacts'),
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    topic = models.CharField(
        max_length=200,
        help_text=('This will appear in the contact form dropdown list'),
    )
    contact = models.ManyToManyField(
        Contact,
        blank=True,
        help_text=('Who should messages for this topic be sent to? '),
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['topic']

    def __str__(self):
        return self.topic


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    topic = models.ForeignKey(
        Topic,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'messages received'
        verbose_name_plural = 'messages received'
