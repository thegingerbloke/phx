import json

from django import template

register = template.Library()


@register.filter()
def pretty_print(value):
    return json.dumps(value, indent=4)
