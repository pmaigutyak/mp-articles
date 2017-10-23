
from django.apps import apps
from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_latest_articles(context, article_type, count=5):

    site_model = apps.get_model('sites', 'Site')

    site = site_model.objects.get(domain=context.request.META.get('HTTP_HOST'))

    return apps.get_model('articles', 'Article').objects.filter(
        type__slug=article_type, site=site)[:count]


@register.simple_tag(takes_context=True)
def get_most_popular_articles(context, article_type, count=5):

    site_model = apps.get_model('sites', 'Site')

    site = site_model.objects.get(domain=context.request.META.get('HTTP_HOST'))

    return apps.get_model('articles', 'Article').most_popular(
        site.id, article_type)[:count]
