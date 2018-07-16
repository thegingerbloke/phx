from django import template
from django.templatetags import static

register = template.Library()


# from:
# https://simpleisbetterthancomplex.com/snippet/2016/08/22/dealing-with-querystring-parameters.html
@register.simple_tag
def url_self_with_params(field_name, value, urlencode=None):
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(
            lambda p: p.split('=')[0] != field_name, querystring
        )
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url


class AbsoluteStaticNode(static.StaticNode):
    def url(self, context):
        request = context['request']
        return request.build_absolute_uri(super().url(context))


@register.tag('absolutestatic')
def absolutestatic(parser, token):
    return AbsoluteStaticNode.handle_token(parser, token)


@register.simple_tag(takes_context=True)
def absolutemedia(context, media_url):
    request = context['request']
    return '{0}://{1}{2}'.format(request.scheme, request.get_host(), media_url)
