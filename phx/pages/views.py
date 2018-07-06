from django.shortcuts import get_object_or_404, render
from .models import Page


def index(request, slug):
    slug = '/{0}'.format(slug)
    if not slug.endswith('/'):
        slug = '{0}/'.format(slug)
    page = get_object_or_404(Page, slug=slug)
    top_level_page = get_top_level_page(page)
    subnav = generate_subnav(slug, top_level_page)
    breadcrumb = generate_breadcrumb(slug, page)
    return render(request, 'pages/page.html', {
        'page': page,
        'subnav': subnav,
        'breadcrumb': breadcrumb,
    })


def generate_subnav(slug, page):
    pages = []
    children = page.children.all()

    for child in children:
        pages.append({
            'title': child.title,
            'linkUrl': child.slug,
            'active': child.slug == slug,
            'children': generate_subnav(slug, child)
        })
    return pages


def get_top_level_page(page):
    if page.parent:
        page = get_top_level_page(page.parent)
    return page


def generate_breadcrumb(slug, page):
    breadcrumb_segments = []
    generate_breadcrumb_segment(
        slug,
        page,
        breadcrumb_segments,
    )
    breadcrumb_segments.insert(0, {
        'title': 'Home',
        'linkUrl': '/',
    })
    return breadcrumb_segments


def generate_breadcrumb_segment(slug, page, breadcrumb_segments):
    breadcrumb_segments.insert(0, {
        'title': page.title,
        'linkUrl': None if slug == page.slug else page.slug,
    })
    if page.parent:
        generate_breadcrumb_segment(slug, page.parent, breadcrumb_segments)
