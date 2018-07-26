from phx.admin import phx_admin
from .models import (Page, Component, Editorial, Feature, Quote, Image,
                     ListItems)
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


class PageAdmin(nested_admin.NestedModelAdmin):
    list_display = ['get_title', 'parent', 'slug']
    ordering = ['slug']

    def get_title(self, obj):
        if obj.parent and obj.parent.parent:
            title = '⤚⤍ {0}'.format(obj.title)
        elif obj.parent:
            title = '↣ {0}'.format(obj.title)
        else:
            title = obj.title
        return title
    get_title.short_description = 'title'

    # if adding, hide readonly fixture detail field
    def get_readonly_fields(self, request, obj):
        return [] if obj is None else ['slug']

    # if adding, hide slug select field
    def get_exclude(self, request, obj):
        return ['author'] if obj is None else ['author', 'slug']

    # fieldsets = (
    #     ('Content', {
    #         'fields': ('title', 'slug', 'summary', 'content', 'parent')
    #     }),
    #     ('Dates', {
    #         'fields': ('live_start_date', 'live_end_date')
    #     }),
    # )
    inlines = [ComponentAdmin]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


phx_admin.register(Page, PageAdmin)
