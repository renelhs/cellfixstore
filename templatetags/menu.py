import re
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, url_name):
    """
    A filter tag to select active link in navbar
    :param url_name: url_name
    :param context: context
    :return: class
    """
    path = context['request'].path
    all_url_names = url_name.split('|')

    if all_url_names:
        for pattern in all_url_names:
            if re.search(pattern, path) and pattern != '':
                return 'active'

    return ''
