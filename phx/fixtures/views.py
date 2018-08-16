from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404
from phx.helpers.subnav import generate_subnav
from components.models import COMPONENT_TYPES
from pages.models import Page, Component
from .models import Fixture, Category


class FixturesListView(generic.ListView):
    model = Fixture

    def get_context_data(self, **kwargs):
        context = super(FixturesListView, self).get_context_data(**kwargs)
        context['breadcrumb'] = self.generate_breadcrumb()

        slug = self.request.path
        page = get_object_or_404(Page, slug=slug)
        context['page'] = page
        context['page_title'] = page.title
        context['components'] = Component.objects.select_related(
            *COMPONENT_TYPES
        ).filter(page_id=page.id)

        context['categories'] = Category.objects.all()
        context['subnav'] = generate_subnav(slug, page)
        return context

    def get_queryset(self):
        return Fixture.objects.prefetch_related('categories').filter(
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
