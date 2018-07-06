from django.utils import timezone
from django.shortcuts import render
from news.models import News
from results.models import Results
from fixtures.models import Fixtures
import json


def index(request):
    with open('../frontend/components/global/GridBlocks/demo/demo.json') as f:
        data = json.load(f)

    fixtures = Fixtures.objects.filter(
        event_date__gte=timezone.now()
    ).order_by('event_date')[:3]

    results = Results.objects.filter(
        fixture__event_date__lte=timezone.now()
    ).order_by('-fixture__event_date')[:3]

    news = News.objects.all().order_by('-created_date')[:3]

    data['fixtures']['data'] = fixtures
    data['results']['data'] = results
    data['news']['data'] = news

    context = {
        'data': data
    }

    return render(request, 'home/home.html', context)
