import datetime
from django import template
from django.utils.timezone import now

register = template.Library()

@register.filter
def short_time_ago(value):
    """
    Converts a datetime into Instagram/YouTube-style time:
    - "5m" (minutes)
    - "2h" (hours)
    - "3d" (days)
    - "1w" (weeks)
    - "2mo" (months)
    - "1y" (years)
    """
    if not value:
        return ""

    delta = now() - value

    if delta.total_seconds() < 60:
        return "Now"
    elif delta.total_seconds() < 3600:
        return f"{int(delta.total_seconds() // 60) } minitues ago"
    elif delta.total_seconds() < 86400:
        return f"{int(delta.total_seconds() // 3600)} hours ago"
    elif delta.total_seconds() < 604800:
        return f"{int(delta.total_seconds() // 86400)} days ago"
    elif delta.total_seconds() < 2592000:
        return f"{int(delta.total_seconds() // 604800)} weeks ago"
    elif delta.total_seconds() < 31536000:
        return f"{int(delta.total_seconds() // 2592000)} months ago"
    else:
        return f"{int(delta.total_seconds() // 31536000)} years ago"
