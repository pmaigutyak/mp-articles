
from django.db import models
from django.contrib import admin

from easy_select2.widgets import Select2Multiple
from modeltranslation.admin import TranslationAdmin

from articles.models import Article, ArticleTag


class ArticleAdmin(TranslationAdmin):

    list_display = [
        'title', 'type', 'created', 'is_comments_enabled']

    list_filter = ['type', 'created', 'is_comments_enabled']

    formfield_overrides = {
        models.ManyToManyField: {
            'widget': Select2Multiple(select2attrs={'width': '500px'})
        }
    }


class ArticleTagAdmin(TranslationAdmin):

    list_display = ['text']
    search_fields = ['text']


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleTag, ArticleTagAdmin)
