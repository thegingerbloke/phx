from django.contrib import admin
from phx.admin import phx_admin
from .models import Category, Fixture


class FixtureAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'location', 'has_results']
    list_select_related = ['fixture']
    ordering = ['-event_date']
    exclude = ['author']

    def has_results(self, obj):
        return True if obj.fixture else False
        # return obj.results
    has_results.boolean = True

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'abbreviation']
    pass


phx_admin.register(Category, CategoryAdmin)
phx_admin.register(Fixture, FixtureAdmin)
