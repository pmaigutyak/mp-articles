
import articles.translation

from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from articles.models import Article


class ArticleAdmin(TranslationAdmin):

    list_display = ['title', 'type']

    list_filter = ['type']


admin.site.register(Article, ArticleAdmin)
