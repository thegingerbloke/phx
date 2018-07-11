from django.contrib import admin
from .models import Categories, Fixtures


class FixturesAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'location', 'has_results')
    ordering = ('-event_date',)
    exclude = ('author',)

    def has_results(self, obj):
        return True if obj.fixture else False
        # return obj.results
    has_results.boolean = True

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


class CategoriesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Fixtures, FixturesAdmin)
