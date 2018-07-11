from django.contrib import admin
from .models import (News, Thumbnails, Components, Editorials, Features,
                     Quotes, Images, ListItems)
from components.admin import (AbstractEditorialsAdmin, AbstractFeaturesAdmin,
                              AbstractListItemsAdmin, AbstractQuotesAdmin,
                              AbstractImagesAdmin)
import nested_admin


class EditorialsAdmin(AbstractEditorialsAdmin):
    model = Editorials


class FeaturesAdmin(AbstractFeaturesAdmin):
    model = Features


class ListItemsAdmin(AbstractListItemsAdmin):
    model = ListItems


class QuotesAdmin(AbstractQuotesAdmin):
    model = Quotes


class ImagesAdmin(AbstractImagesAdmin):
    model = Images


class ComponentsAdmin(nested_admin.NestedStackedInline):
    model = Components
    extra = 0
    inlines = [
        EditorialsAdmin,
        FeaturesAdmin,
        ListItemsAdmin,
        QuotesAdmin,
        ImagesAdmin,
    ]
    # exclude = ['order']
    sortable_field_name = 'order'


class ThumbnailsAdmin(nested_admin.NestedStackedInline):
    model = Thumbnails


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
    inlines = [ThumbnailsAdmin, ComponentsAdmin]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(News, NewsAdmin)
