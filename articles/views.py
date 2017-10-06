
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from pure_pagination import PaginationMixin
from hitcount.views import HitCountDetailView

from articles.settings import ARTICLE_TYPE_CHOICES
from articles.models import Article


class ArticleListView(PaginationMixin, ListView):

    template_name = 'articles/list.html'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(type=self.kwargs['type'])

    def get_context_data(self, **kwargs):
        cxt = super(ArticleListView, self).get_context_data(**kwargs)
        cxt['printable_article_type'] = (
            dict(ARTICLE_TYPE_CHOICES)[self.kwargs['type']])
        return cxt


class ArticleDetailView(HitCountDetailView):

    template_name = 'articles/info.html'
    count_hit = True

    def get_object(self, queryset=None):
        query = {
            'type': self.kwargs['type'],
            'pk': self.kwargs['id']
        }
        return get_object_or_404(Article, **query)
