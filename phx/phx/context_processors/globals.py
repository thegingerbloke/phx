from django.conf import settings


def globals(request):
    """Expose config values to templates"""
    return {
        'SITE_TITLE': settings.SITE_TITLE,
        'SITE_DESCRIPTION': settings.SITE_DESCRIPTION,
    }
