
from django.db import models
from django.contrib import admin

from easy_select2.widgets import Select2Multiple
from modeltranslation.admin import TranslationAdmin

from articles.models import Article, ArticleTag, ArticleType


class ArticleAdmin(TranslationAdmin):

    list_display = [
        'title', 'type', 'site', 'created', 'is_comments_enabled']

    list_filter = ['site', 'type', 'created', 'is_comments_enabled']

    formfield_overrides = {
        models.ManyToManyField: {
            'widget': Select2Multiple(select2attrs={'width': '500px'})
        }
    }


class ArticleTagAdmin(TranslationAdmin):

    list_display = ['text']
    search_fields = ['text']


class ArticleTypeAdmin(TranslationAdmin):

    list_display = ['name']
    search_fields = ['name']


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleTag, ArticleTagAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
