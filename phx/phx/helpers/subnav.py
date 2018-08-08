def generate_subnav(slug, page):
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
