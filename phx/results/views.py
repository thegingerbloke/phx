from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .models import Results
from pages.models import Page


def index(request):
    breadcrumb = generate_breadcrumb()
    page = get_object_or_404(Page, slug=request.path)
    results = Results.objects.filter(
        fixture__event_date__lte=timezone.now()
    ).order_by('fixture__event_date')
    return render(request, 'results/results.html', {
        'page': page,
        'breadcrumb': breadcrumb,
        'results': results
    })


def generate_breadcrumb():
    return [
        {
            'title': 'Home',
            'linkUrl': '/',
        },
        {
            'title': 'Results',
        }
    ]