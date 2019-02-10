from django.contrib import admin
from django.utils.html import format_html
from easy_thumbnails.files import get_thumbnailer

from phx.admin import phx_admin

from .models import Gallery, Image, Thumbnail


class ImageAdmin(admin.StackedInline):
    model = Image
    readonly_fields = ['current_image']
    extra = 1

    def current_image(self, obj):
        thumbnailer = get_thumbnailer(obj.image)
        thumbnail_options = {'size': (200, 200)}
        return format_html('<img src="/media/{0}" />'.format(
            thumbnailer.get_thumbnail(thumbnail_options)))


class ThumbnailAdmin(admin.StackedInline):
    model = Thumbnail
    readonly_fields = ['current_image']

    def current_image(self, obj):
        thumbnailer = get_thumbnailer(obj.image)
        thumbnail_options = {'size': (200, 200)}
        return format_html('<img src="/media/{0}" />'.format(
            thumbnailer.get_thumbnail(thumbnail_options)))


class GalleryAdmin(admin.ModelAdmin):
    list_display = [
        'get_thumbnail', 'title', 'created_date', 'author', 'image_count'
    ]
    list_display_links = ['get_thumbnail', 'title']
    list_select_related = ['author', 'thumbnail']
    list_prefetch_related = ['images']
    search_fields = ['title']
    readonly_fields = ['slug']
    exclude = ['author']
    inlines = [ThumbnailAdmin, ImageAdmin]

    def image_count(self, obj):
        return obj.images.count()

    def get_thumbnail(self, obj):
        thumbnailer = get_thumbnailer(obj.thumbnail.image)
        thumbnail_options = {'size': (100, 100)}
        return format_html('<img src="/media/{0}" />'.format(
            thumbnailer.get_thumbnail(thumbnail_options)))

    get_thumbnail.short_description = 'thumbnail'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


phx_admin.register(Gallery, GalleryAdmin)
