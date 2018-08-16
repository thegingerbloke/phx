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
    list_select_related = ['parent']
    autocomplete_fields = ['parent']
    search_fields = ['title', 'parent__title']
    ordering = ['slug']
    inlines = [ComponentAdmin]

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

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    # base PageAdmin form doesn't contain files,
    # so doesn't register as requring multipart support (`has_file_field`)
    # this fix ensures `enctype="multipart/form-data"` is added to HTML form
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.is_multipart = lambda n: True
        return form


phx_admin.register(Page, PageAdmin)
