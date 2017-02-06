
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


DEFAULT_ARTICLE_TYPE_CHOICES = (
    ('news', _('News')),
)


ARTICLE_TYPE_CHOICES = getattr(
    settings, 'ARTICLE_TYPE_CHOICES', DEFAULT_ARTICLE_TYPE_CHOICES)


DEFAULT_ARTICLE_TYPE = getattr(settings, 'DEFAULT_ARTICLE_TYPE', None)
