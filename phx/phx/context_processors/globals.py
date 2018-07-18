from django.conf import settings


def globals(request):
    """Expose config values to templates"""
    config = {
        'HOST': settings.HOST,
        'SITE_TITLE': settings.SITE_TITLE,
        'SITE_DESCRIPTION': settings.SITE_DESCRIPTION,
    }

    if hasattr(settings, 'ANALYTICS'):
        config['ANALYTICS'] = settings.ANALYTICS

    return config
