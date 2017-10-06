
from django.apps import apps
from django import template


register = template.Library()


@register.simple_tag
def get_latest_articles(article_type, count=5):
    return apps.get_model('articles', 'Article').objects.filter(
        type=article_type)[:count]


@register.simple_tag
def get_most_popular_articles(article_type, count=5):
    return apps.get_model('articles', 'Article').most_popular(
        article_type)[:count]
