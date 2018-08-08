from django.utils.html import format_html
from phx.admin import phx_admin
from .models import (News, Thumbnail, Component, Editorial, Feature,
                     Quote, Image, ListItems)
from components.admin import (AbstractEditorialAdmin, AbstractFeatureAdmin,
                              AbstractListItemsAdmin, AbstractQuoteAdmin,
                              AbstractImageAdmin)
import nested_admin


class EditorialAdmin(AbstractEditorialAdmin):
    model = Editorial


class FeatureAdmin(AbstractFeatureAdmin):
    model = Feature


class ListItemsAdmin(AbstractListItemsAdmin):
    model = ListItems


class QuoteAdmin(AbstractQuoteAdmin):
    model = Quote


class ImageAdmin(AbstractImageAdmin):
    model = Image


class ComponentAdmin(nested_admin.NestedStackedInline):
    model = Component
    extra = 0
    inlines = [
        EditorialAdmin,
        FeatureAdmin,
        ListItemsAdmin,
        QuoteAdmin,
        ImageAdmin,
    ]
    sortable_field_name = 'order'


class ThumbnailAdmin(nested_admin.NestedStackedInline):
    model = Thumbnail
    readonly_fields = ['current_image']

    def current_image(self, obj):
        return format_html(
            '<img src="{0}" style="max-width:200px" />'.format(
                obj.image.url
            )
        )


class NewsAdmin(nested_admin.NestedModelAdmin):
    list_display = ['current_image', 'title', 'created_date', 'author']
    list_display_links = ['current_image', 'title']

    exclude = ['author']

    def current_image(self, obj):
        return format_html(
            '<img src="{0}" style="max-width:100px" />'.format(
                obj.thumbnail.image.url
            )
        )

    # fieldsets = (
    #     ('Story', {
    #         'fields': ('title', 'summary', 'content')
    #     }),
    #     ('Dates', {
    #         'fields': ('live_start_date', 'live_end_date')
    #     }),
    # )
    inlines = [ThumbnailAdmin, ComponentAdmin]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


phx_admin.register(News, NewsAdmin)
