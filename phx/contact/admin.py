from django.contrib import admin
from .models import Contact, Topic, Message


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic', 'contacts', 'created_date')

    def contacts(self, obj):
        return ', '.join([contact.name for contact in obj.contact.all()])

    contacts.short_description = 'Contacts'


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'topic', 'message_received')
    readonly_fields = ('name', 'email', 'topic', 'message', 'created_date')

    def message_received(self, obj):
        return obj.created_date

    def has_add_permission(self, request):
        return False


admin.site.register(Contact, ContactAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)

