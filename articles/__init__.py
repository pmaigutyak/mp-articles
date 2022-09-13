
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArticlesConfig(AppConfig):
    name = 'articles'
    verbose_name = _("Articles")


default_app_config = 'articles.ArticlesConfig'
