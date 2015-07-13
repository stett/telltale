from django import template
from django.utils.safestring import mark_safe
from markdown2 import markdown as _markdown

register = template.Library()


@register.filter
def markdown(value):
    return mark_safe(_markdown(value))
