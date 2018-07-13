from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Fixtures, Categories
from pages.views import generate_subnav
from pages.models import Page


class FixturesListView(generic.ListView):
    model = Fixtures

    def get_context_data(self, **kwargs):
        context = super(FixturesListView, self).get_context_data(**kwargs)
        context['breadcrumb'] = self.generate_breadcrumb()
        context['page'] = get_object_or_404(Page, slug=self.request.path)
        context['categories'] = Categories.objects.all()
        context['subnav'] = generate_subnav(self.request.path, context['page'])
        return context

    def get_queryset(self):
        return Fixtures.objects.filter(
            event_date__gte=timezone.now(),
        ).order_by('event_date')

    def generate_breadcrumb(self):
        return [
            {
                'title': 'Home',
                'linkUrl': '/',
            },
            {
                'title': 'Fixtures',
            }
        ]
