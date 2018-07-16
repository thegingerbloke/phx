from django.views import generic
from django.urls import reverse
from django.db.models import Q
from .models import News


class NewsListView(generic.ListView):
    model = News
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['breadcrumb'] = self.generate_breadcrumb()
        context['search'] = self.request.GET.get('search', '')
        # context['page'] = get_object_or_404(Page, slug=self.request.path)
        return context

    def get_queryset(self):
        query = News.objects.all().distinct()

        search = self.request.GET.get('search')
        if search:
            query = query.filter(
                Q(title__icontains=search) |
                Q(summary__icontains=search) |
                Q(components__editorial__content__icontains=search)
            )

        return query

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
        context['data'] = {
            "previous": self.get_previous(),
            "next": self.get_next(),
        }
        return context

    def get_previous(self):
        id = self.get_object().id
        previous = News.objects.filter(id__lt=id).order_by('-id')[0:1].first()
        if previous:
            return {
                'title': previous.title,
                'link_url': reverse('news-detail', kwargs={
                    'pk': previous.id,
                    'slug': previous.slug
                })
            }

    def get_next(self):
        id = self.get_object().id
        next = News.objects.filter(id__gt=id).order_by('id')[0:1].first()
        if next:
            return {
                'title': next.title,
                'link_url': reverse('news-detail', kwargs={
                    'pk': next.id,
                    'slug': next.slug
                })
            }

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
