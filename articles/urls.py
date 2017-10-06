
from django.conf.urls import url

from articles import views


urlpatterns = [

    url(r'^(?P<type>\w+)/$', views.ArticleListView.as_view(), name='list'),

    url(r'^(?P<type>\w+)/(?P<slug>\w+)_(?P<id>\d+)/$',
        views.ArticleDetailView.as_view(), name='info')

]
