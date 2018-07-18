from django import template

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
