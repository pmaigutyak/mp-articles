
from django.conf.urls import url

from articles.views import article_list, article_info


urlpatterns = [

    url(r'^(?P<article_type>\w+)/$', article_list, name='list'),

    url(r'^(?P<article_type>\w+)/(?P<article_id>\d+)/$', article_info,
        name='info')

]
