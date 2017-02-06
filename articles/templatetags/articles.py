
from django.apps import apps
from django import template


register = template.Library()


@register.simple_tag
def get_latest_articles(article_type, count=5):
    return apps.get_model('articles', 'Article').objects.filter(
        type=article_type).order_by('-id')[:count]
