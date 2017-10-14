
from modeltranslation.translator import register, TranslationOptions

from articles.models import Article, ArticleTag


@register(Article)
class ArticleTranslationOptions(TranslationOptions):

    fields = ('title', 'description', 'text', )


@register(ArticleTag)
class ArticleTagTranslationOptions(TranslationOptions):

    fields = ('text', )
