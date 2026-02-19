from django import template

register=template.Library()


def swap(value):
    return value.swapcase()


@register.filter('r')
def replace(value,s):
    return value.replace(s,'F')




register.filter('s',swap)