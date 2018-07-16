from django.contrib import admin
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
    # exclude = ['order']
    sortable_field_name = 'order'


class ThumbnailAdmin(nested_admin.NestedStackedInline):
    model = Thumbnail


class NewsAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title', 'created_date', 'author')
    exclude = ['author']
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


admin.site.register(News, NewsAdmin)
