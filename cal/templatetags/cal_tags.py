from django import template

register = template.Library()


@register.simple_tag
def compare_users(entry_user, request_user):
    if entry_user == request_user:
        return True
    return False
