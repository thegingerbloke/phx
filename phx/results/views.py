from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Results
from fixtures.models import Categories
from pages.models import Page


class ResultsListView(generic.ListView):
    model = Results
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(ResultsListView, self).get_context_data(**kwargs)
        context['breadcrumb'] = self.generate_breadcrumb()
        context['page'] = get_object_or_404(Page, slug=self.request.path)
        context['categories'] = Categories.objects.all()
        context['search'] = self.request.GET.get('search', '')
        context['category'] = self.request.GET.get('category', '')
        return context

    def get_queryset(self):
        query = Results.objects.filter(
            fixture__event_date__lte=timezone.now(),
        ).order_by('-fixture__event_date')

        search = self.request.GET.get('search')
        if search:
            query = query.filter(
                Q(summary__icontains=search) |
                Q(results__icontains=search) |
                Q(fixture__title__icontains=search) |
                Q(fixture__description__icontains=search) |
                Q(fixture__location__icontains=search) |
                Q(fixture__categories__abbreviation__icontains=search) |
                Q(fixture__categories__title__icontains=search)
            )

        category = self.request.GET.get('category')
        if category:
            query = query.filter(fixture__categories__abbreviation=category)

        return query

    def generate_breadcrumb(self):
        return [
            {
                'title': 'Home',
                'linkUrl': '/',
            },
            {
                'title': 'Results',
            }
        ]
