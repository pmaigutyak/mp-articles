
from modeltranslation.translator import register, TranslationOptions

from articles.models import Article, ArticleTag, ArticleType


@register(Article)
class ArticleTranslationOptions(TranslationOptions):

    fields = ('title', 'description', 'text', )


@register(ArticleTag)
class ArticleTagTranslationOptions(TranslationOptions):

    fields = ('text', )


@register(ArticleType)
class ArticleTypeTranslationOptions(TranslationOptions):

    fields = ('name', )
