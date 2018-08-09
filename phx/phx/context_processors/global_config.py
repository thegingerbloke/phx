from django.conf import settings


def global_config(request):
    """
    Add config info to the global template context
    """
    config = {
        'HOST': settings.HOST,
        'SITE_TITLE': settings.SITE_TITLE,
        'SITE_DESCRIPTION': settings.SITE_DESCRIPTION,
    }

    if hasattr(settings, 'ANALYTICS'):
        config['ANALYTICS'] = settings.ANALYTICS

    return config
