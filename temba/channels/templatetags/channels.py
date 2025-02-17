from django import template

register = template.Library()


@register.filter
def channel_icon(channel):
    return channel.type.icon
