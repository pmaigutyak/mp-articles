
from modeltranslation.translator import register, TranslationOptions

from articles.models import Article


@register(Article)
class FlatPageTranslationOptions(TranslationOptions):

    fields = ('title', 'description', 'text', )
