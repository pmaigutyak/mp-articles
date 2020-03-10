
from django.conf import settings

from articles import defaults


IS_ARTICLE_TYPE_ENABLED = getattr(
    settings, 'IS_ARTICLE_TYPE_ENABLED', defaults.IS_ARTICLE_TYPE_ENABLED)

IS_ARTICLE_HITCOUNT_ENABLED = getattr(
    settings, 'IS_ARTICLE_HITCOUNT_ENABLED', False)

IS_ARTICLE_TAGS_ENABLED = getattr(
    settings, 'IS_ARTICLE_TAGS_ENABLED', False)

IS_ARTICLE_COMMENTS_ENABLED = getattr(
    settings, 'IS_ARTICLE_COMMENTS_ENABLED', False)
