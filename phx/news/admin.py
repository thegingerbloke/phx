from easy_thumbnails.files import get_thumbnailer
from django.utils.html import format_html
from phx.admin import phx_admin
from .models import (
    News,
    Thumbnail,
    Component,
    Editorial,
    Embed,
    Feature,
    Image,
    ListItems,
    Quote,
    Table,
)
from components.admin import (
    AbstractEditorialAdmin,
    AbstractEmbedAdmin,
    AbstractFeatureAdmin,
    AbstractImageAdmin,
    AbstractListItemsAdmin,
    AbstractQuoteAdmin,
    AbstractTableAdmin,
)
import nested_admin


class EditorialAdmin(AbstractEditorialAdmin):
    model = Editorial


class EmbedAdmin(AbstractEmbedAdmin):
    model = Embed


class FeatureAdmin(AbstractFeatureAdmin):
    model = Feature


class ImageAdmin(AbstractImageAdmin):
    model = Image


class ListItemsAdmin(AbstractListItemsAdmin):
    model = ListItems


class QuoteAdmin(AbstractQuoteAdmin):
    model = Quote


class TableAdmin(AbstractTableAdmin):
    model = Table


class ComponentAdmin(nested_admin.NestedStackedInline):
    model = Component
    extra = 0
    inlines = [
        EditorialAdmin,
        EmbedAdmin,
        FeatureAdmin,
        ImageAdmin,
        ListItemsAdmin,
        QuoteAdmin,
        TableAdmin,
    ]
    sortable_field_name = 'order'


class ThumbnailAdmin(nested_admin.NestedStackedInline):
    model = Thumbnail
    readonly_fields = ['current_image']

    def current_image(self, obj):
        thumbnailer = get_thumbnailer(obj.image)
        thumbnail_options = {'size': (200, 200)}
        return format_html(
            '<img src="/media/{0}" />'.format(
                thumbnailer.get_thumbnail(thumbnail_options)
            )
        )


class NewsAdmin(nested_admin.NestedModelAdmin):
    list_display = ['current_image', 'title', 'created_date', 'author']
    list_display_links = ['current_image', 'title']
    list_select_related = ['author', 'thumbnail']
    exclude = ['author']
    inlines = [ThumbnailAdmin, ComponentAdmin]

    def current_image(self, obj):
        thumbnailer = get_thumbnailer(obj.thumbnail.image)
        thumbnail_options = {'size': (100, 100)}
        return format_html(
            '<img src="/media/{0}" />'.format(
                thumbnailer.get_thumbnail(thumbnail_options)
            )
        )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


phx_admin.register(News, NewsAdmin)
