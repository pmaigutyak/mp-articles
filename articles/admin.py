
import articles.translation

from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from articles.models import Article


class ArticleAdmin(TranslationAdmin):

    list_display = [
        'title', 'type', 'created', 'is_comments_enabled']

    list_filter = ['type', 'created', 'is_comments_enabled']


admin.site.register(Article, ArticleAdmin)
