from django import template

register = template.Library()


@register.simple_tag
def compare_users(entry_user, request_user):
    return entry_user == request_user
