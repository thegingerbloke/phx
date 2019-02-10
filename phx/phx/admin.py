from django.contrib.admin import AdminSite
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User


class PHXAdminSite(AdminSite):
    site_title = 'Brighton Phoenix - Administration'
    site_header = 'Brighton Phoenix - Administration'


phx_admin = PHXAdminSite()
phx_admin.register(Group, GroupAdmin)
phx_admin.register(User, UserAdmin)
