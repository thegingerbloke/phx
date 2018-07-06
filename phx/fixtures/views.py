from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .models import Fixtures
from pages.models import Page


def index(request):
    breadcrumb = generate_breadcrumb()
    page = get_object_or_404(Page, slug=request.path)
    fixtures = Fixtures.objects.filter(
        event_date__gte=timezone.now()
    ).order_by('event_date')

    return render(request, 'fixtures/fixtures.html', {
        'page': page,
        'fixtures': fixtures,
        'breadcrumb': breadcrumb
    })


def generate_breadcrumb():
    return [
        {
            'title': 'Home',
            'linkUrl': '/',
        },
        {
            'title': 'Fixtures',
        }
    ]