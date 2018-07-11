from django.contrib import admin
from .models import (Page, Components, Editorials, Features, Quotes, Images,
                     ListItems)
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


class PageAdmin(nested_admin.NestedModelAdmin):
    # list display config
    list_display = ('get_title', 'parent', 'slug', )
    ordering = ('slug', )

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
    inlines = [ComponentsAdmin]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Page, PageAdmin)
