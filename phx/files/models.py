from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from phx.helpers.file import file_size_string


def file_size_validator(value):
    limit = 10 * 1024 * 1024
    if value.size > limit:
        file_size = file_size_string(value.size)
        limit_size = file_size_string(limit)
        error = (
            'File is too large - {0}. '
            'It should not exceed {1}'
        ).format(file_size, limit_size)
        raise ValidationError(error)


class File(models.Model):
    file = models.FileField(
      upload_to='file',
      validators=[file_size_validator]
    )
    title = models.CharField(
        max_length=200,
        blank=True,
        help_text=(
          'This is isn\'t displayed on the website but helps us to identify'
          'the file in the admin'
        ),
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.file.url
