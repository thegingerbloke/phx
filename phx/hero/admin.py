from easy_thumbnails.files import get_thumbnailer
from django.utils.html import format_html
from django.contrib import admin
from phx.admin import phx_admin
from .models import Hero


class HeroAdmin(admin.ModelAdmin):
    list_display = ['current_image', 'caption', 'created_date', 'author']
    list_display_links = ['current_image', 'caption']
    readonly_fields = ['current_image']
    exclude = ['author']

    def current_image(self, obj):
        thumbnailer = get_thumbnailer(obj.image)
        thumbnail_options = {'size': (200, 200)}
        return format_html(
            '<img src="/media/{0}" />'.format(
                thumbnailer.get_thumbnail(thumbnail_options)
            )
        )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


phx_admin.register(Hero, HeroAdmin)
