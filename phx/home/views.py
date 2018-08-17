from itertools import chain
from django.views import generic
from django.utils import timezone
from news.models import News
from results.models import Result
from fixtures.models import Fixture
from .models import Content, Announcement, Hero, HeroImageCategory


class HomeView(generic.TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        self.content = Content.objects.first()
        context = super(HomeView, self).get_context_data(**kwargs)
        context['about'] = self.get_about()
        context['announcement'] = self.get_announcement()
        context['events'] = self.get_events()
        context['fixtures'] = self.get_fixtures()
        context['gallery'] = self.get_gallery()
        context['heroes'] = self.get_heroes()
        context['join'] = self.get_join()
        context['news'] = self.get_news()
        context['results'] = self.get_results()
        context['title'] = self.get_title()
        return context

    def get_about(self):
        return self.content.about

    def get_announcement(self):
        annoucement = Announcement.objects.filter(
            display_until__gte=timezone.now()
        ).order_by('-created_date')[:1].first()
        if annoucement:
            return annoucement.announcement

    def get_events(self):
        return self.content.events

    def get_fixtures(self):
        return Fixture.objects.filter(
            event_date__gte=timezone.now()
        ).order_by('event_date')[:5]

    def get_gallery(self):
        return self.content.gallery

    def get_heroes(self):
        """
        Select the desired number of hero images for each category
        Ensure each query excludes hero images that have already been returned
        """
        categories = HeroImageCategory.objects.all()
        heroes = []
        exclude_ids = []
        for category in categories:
            queryset = Hero.objects.filter(
                image_categories=category
            ).order_by('?').exclude(id__in=exclude_ids)[:category.count]
            exclude_ids = exclude_ids + [hero.id for hero in queryset]
            heroes = chain(heroes, queryset)
        return list(heroes)

    def get_join(self):
        return self.content.join

    def get_news(self):
        return News.objects.select_related('thumbnail').all().order_by(
            '-created_date'
        )[:3]

    def get_results(self):
        return Result.objects.select_related('fixture').filter(
            fixture__event_date__lte=timezone.now()
        ).order_by('-fixture__event_date')[:5]

    def get_title(self):
        return self.content.title
