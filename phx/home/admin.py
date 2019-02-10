from django.contrib import admin
from django.utils.html import format_html, strip_tags
from easy_thumbnails.files import get_thumbnailer

from phx.admin import phx_admin

from .models import Announcement, Content, Hero, HeroImageCategory


class ContentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['gallery']

    def has_add_permission(self, *args, **kwargs):
        return not Content.objects.exists()


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = [
        'get_announcement', 'created_date', 'display_until', 'author'
    ]
    exclude = ['author']

    def get_announcement(self, obj):
        return strip_tags(obj.announcement)

    get_announcement.short_description = 'announcement'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


class HeroAdmin(admin.ModelAdmin):
    list_display = [
        'current_image', 'caption', 'categories', 'created_date', 'author'
    ]
    list_display_links = ['current_image', 'caption']
    readonly_fields = ['current_image']
    exclude = ['author']

    def categories(self, obj):
        return ', '.join([cat.category for cat in obj.image_categories.all()])

    def current_image(self, obj):
        thumbnailer = get_thumbnailer(obj.image)
        thumbnail_options = {'size': (200, 200)}
        return format_html('<img src="/media/{0}" />'.format(
            thumbnailer.get_thumbnail(thumbnail_options)))

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


class HeroImageCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'count']


phx_admin.register(Content, ContentAdmin)
phx_admin.register(Announcement, AnnouncementAdmin)
phx_admin.register(Hero, HeroAdmin)
phx_admin.register(HeroImageCategory, HeroImageCategoryAdmin)
