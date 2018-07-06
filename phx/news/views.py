from django.views import generic
from django.urls import reverse
from .models import News


class NewsListView(generic.ListView):
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['breadcrumb'] = self.generate_breadcrumb()
        return context

    def generate_breadcrumb(self):
        return [
            {
                'title': 'Home',
                'linkUrl': '/',
            },
            {
                'title': 'News',
            }
        ]


class NewsDetailView(generic.DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['breadcrumb'] = self.generate_breadcrumb()
        return context

    def generate_breadcrumb(self):
        breadcrumb = [
            {
                'title': 'Home',
                'linkUrl': '/',
            },
            {
                'title': 'News',
                'linkUrl': reverse('news-list'),
            },
            {
                'title': self.get_object().title
            }
        ]
        return breadcrumb
