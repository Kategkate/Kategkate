import time

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.simple_tag
def get_time():
    return time.ctime()


@register.filter
@stringfilter
def inversion(value):
    return value[::-1]
