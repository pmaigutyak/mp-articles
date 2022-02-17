
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from articles.config import IS_ARTICLE_TYPE_ENABLED
from articles import views


app_name = 'articles'

type_prefix = '<str:type>/' if IS_ARTICLE_TYPE_ENABLED else ''


urlpatterns = [

    path(type_prefix, views.ArticleListView.as_view(), name='list'),

    path(type_prefix + '<str:slug>_<int:id>/',
         views.ArticleDetailView.as_view(), name='info')

]

app_urls = i18n_patterns(
    path('articles/', include((urlpatterns, app_name))),
)
