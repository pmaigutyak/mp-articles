
from django.shortcuts import render, get_object_or_404

from pure_pagination import Paginator

from articles.settings import ARTICLE_TYPE_CHOICES
from articles.models import Article


def article_list(request, article_type):

    printable_article_type = dict(ARTICLE_TYPE_CHOICES)[article_type]

    paginator = Paginator(Article.objects.filter(type=article_type), 10)

    context = {
        'printable_article_type': printable_article_type,
        'articles': paginator.page(request.GET.get('page', 1))
    }

    return render(request, 'articles/list.html', context)


def article_info(request, article_type, article_id):

    context = {
        'article': get_object_or_404(Article, type=article_type, id=article_id)
    }

    return render(request, 'articles/info.html', context)
