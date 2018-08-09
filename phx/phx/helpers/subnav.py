def generate_subnav(slug, page):
    """
    Given a slug and a page model instance,
    generate subnav content
    """
    pages = []
    children = page.children.all()

    for child in children:
        pages.append({
            'title': child.title,
            'linkUrl': child.slug,
            'active': child.slug == slug,
            'children': (
                generate_subnav(slug, child) if child.slug in slug else []
            )
        })
    return pages
