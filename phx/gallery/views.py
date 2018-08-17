from django.views import generic
from django.urls import reverse
from django.db.models import Q
from .models import Gallery, Image


class GalleryListView(generic.ListView):
    model = Gallery
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(GalleryListView, self).get_context_data(**kwargs)
        context['breadcrumb'] = self.generate_breadcrumb()
        context['search'] = self.request.GET.get('search', '')
        context['page_title'] = 'Gallery'
        return context

    def get_queryset(self):
        query = Gallery.objects.select_related(
            'thumbnail').prefetch_related('images').all().distinct()

        search = self.request.GET.get('search')
        if search:
            query = query.filter(
                Q(title__icontains=search) |
                Q(summary__icontains=search)
            )

        return query

    def generate_breadcrumb(self):
        return [
            {
                'title': 'Home',
                'linkUrl': '/',
            },
            {
                'title': 'Gallery',
            }
        ]


class GalleryDetailView(generic.DetailView):
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super(GalleryDetailView, self).get_context_data(**kwargs)

        id = self.object.id
        context['images'] = Image.objects.filter(gallery_id=id)

        context['breadcrumb'] = self.generate_breadcrumb()
        context['data'] = {
            "previous": self.get_previous(),
            "next": self.get_next(),
        }
        context['page_title'] = 'Gallery'
        return context

    def get_previous(self):
        id = self.object.id
        previous = Gallery.objects.filter(id__lt=id).order_by(
            '-id')[0:1].first()
        if previous:
            return {
                'title': previous.title,
                'link_url': reverse('gallery-detail', kwargs={
                    'pk': previous.id,
                    'slug': previous.slug
                })
            }

    def get_next(self):
        id = self.object.id
        next = Gallery.objects.filter(id__gt=id).order_by('id')[0:1].first()
        if next:
            return {
                'title': next.title,
                'link_url': reverse('gallery-detail', kwargs={
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
                'title': 'Gallery',
                'linkUrl': reverse('gallery-list'),
            },
            {
                'title': self.object.title
            }
        ]
        return breadcrumb
