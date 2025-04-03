from django import template

register = template.Library()

@register.filter
def dohas_split(value):
    return value.replace(';',';\n')
