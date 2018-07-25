from django.contrib import admin
from phx.admin import phx_admin
from .models import Social


class SocialAdmin(admin.ModelAdmin):
    list_display = [
        'model',
        'title',
        'url',
        'created_date',
        'posted',
        'reposted'
    ]
    readonly_fields = ['model', 'title', 'url', 'posted', 'reposted']

    def has_add_permission(self, request):
        return False


phx_admin.register(Social, SocialAdmin)
