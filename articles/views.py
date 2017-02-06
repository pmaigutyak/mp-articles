
from django.shortcuts import render, get_object_or_404

from pagination import paginate

from articles.models import Article


def article_list(request, article_type):

    printable_article_type = dict(Article.ARTICLE_TYPE_CHOICES)[article_type]

    articles = Article.objects.filter(type=article_type)

    context = {
        'printable_article_type': printable_article_type,
        'articles': paginate(request, articles, items_per_page=10)
    }

    return render(request, 'articles/list.html', context)


def article_info(request, article_type, article_id):

    context = {
        'article': get_object_or_404(Article, type=article_type, id=article_id)
    }

    return render(request, 'articles/info.html', context)
