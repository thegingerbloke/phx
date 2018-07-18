from django.contrib import admin
from django.conf import settings
from phx.admin import phx_admin
from phx.helpers.file import file_size_string
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'url',
        'size',
        'uploaded_by',
        'created_date',
    )
    exclude = ('uploaded_by',)

    def url(self, obj):
        return '{0}{1}'.format(settings.HOST, obj.file.url)

    def size(self, obj):
        return file_size_string(obj.file.size)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'uploaded_by', None) is None:
            obj.uploaded_by = request.user
        obj.save()


phx_admin.register(File, FileAdmin)
