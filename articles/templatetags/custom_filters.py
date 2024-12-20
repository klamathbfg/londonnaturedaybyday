import datetime
from django import template

register = template.Library()

@register.filter
def is_future_date(value):
    if isinstance(value, datetime.datetime):
        value = value.date()
    return value > datetime.date.today()