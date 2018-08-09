from pages.models import Page


def hero(request):
    """
    Add page/hero info to the global template context
    """
    path = request.path

    try:
        page = Page.objects.get(slug=path)
        hero = {
            'title': page.title,
        }
        if page.hero:
            hero['bg'] = page.hero.image
            hero['caption'] = page.hero.caption

    except Page.DoesNotExist:
        hero = {}

    return {
        'hero': hero
    }
