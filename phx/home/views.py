from django.utils import timezone
from django.shortcuts import render
from news.models import News
from results.models import Result
from fixtures.models import Fixture
from hero.models import Hero
import json


def index(request):
    with open('../frontend/components/global/GridBlocks/demo/demo.json') as f:
        data = json.load(f)

    fixtures = Fixture.objects.filter(
        event_date__gte=timezone.now()
    ).order_by('event_date')[:3]

    results = Result.objects.filter(
        fixture__event_date__lte=timezone.now()
    ).order_by('-fixture__event_date')[:3]

    news = News.objects.all().order_by('-created_date')[:3]

    hero = {
        "title": "Welcome",
    }
    random_hero = Hero.objects.order_by('?').first()
    if random_hero:
        hero['bg'] = random_hero.image
        hero['caption'] = random_hero.caption

    data['fixtures']['data'] = fixtures
    data['results']['data'] = results
    data['news']['data'] = news

    # data['announcement'] = {}

    context = {
        'data': data,
        'hero': hero,
    }

    return render(request, 'home/home.html', context)
