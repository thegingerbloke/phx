from components.models import COMPONENT_TYPES
from django.shortcuts import get_object_or_404
from django.views import generic

from phx.helpers.subnav import generate_subnav

from .models import Component, Page


class PageView(generic.TemplateView):
    template_name = "pages/page.html"

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)

        slug = '/{0}'.format(kwargs['slug'])
        if not slug.endswith('/'):
            slug = '{0}/'.format(slug)

        page = get_object_or_404(Page, slug=slug)
        context['page'] = page
        context['page_title'] = page.title
        context['components'] = Component.objects.select_related(
            *COMPONENT_TYPES).filter(page_id=page.id)

        top_level_page = self.get_top_level_page(page)
        context['subnav'] = generate_subnav(slug, top_level_page)
        context['breadcrumb'] = self.generate_breadcrumb(slug, page)

        return context

    def get_top_level_page(self, page):
        if page.parent:
            page = self.get_top_level_page(page.parent)
        return page

    def generate_breadcrumb_segment(self, slug, page, breadcrumb_segments):
        breadcrumb_segments.insert(
            0, {
                'title': page.title,
                'linkUrl': None if slug == page.slug else page.slug,
            })
        if page.parent:
            self.generate_breadcrumb_segment(
                slug,
                page.parent,
                breadcrumb_segments,
            )

    def generate_breadcrumb(self, slug, page):
        breadcrumb_segments = []
        self.generate_breadcrumb_segment(
            slug,
            page,
            breadcrumb_segments,
        )
        breadcrumb_segments.insert(0, {
            'title': 'Home',
            'linkUrl': '/',
        })
        return breadcrumb_segments
