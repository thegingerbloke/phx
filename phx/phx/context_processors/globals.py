from django.conf import settings


def globals(request):
    """Expose config values to templates"""
    return {
        'HOST': settings.HOST,
        'SITE_TITLE': settings.SITE_TITLE,
        'SITE_DESCRIPTION': settings.SITE_DESCRIPTION,
    }
