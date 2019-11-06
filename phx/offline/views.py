from django.views import generic


class OfflineView(generic.TemplateView):
    template_name = "offline/offline.html"
