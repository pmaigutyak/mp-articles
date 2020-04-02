
from random import randint

from django.apps import apps
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property

from articles import config

from ckeditor_uploader.fields import RichTextUploadingField
from slugify import slugify_url


if config.IS_ARTICLE_TYPE_ENABLED:

    class ArticleType(models.Model):

        name = models.CharField(_('Name'), max_length=255, unique=True)

        slug = models.CharField(
            _('Slug'), max_length=255, db_index=True, unique=True)

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = _('Article type')
            verbose_name_plural = _('Article types')


if config.ARE_TAGS_ENABLED:

    class ArticleTag(models.Model):

        text = models.CharField(_('Text'), max_length=255, unique=True)

        def __str__(self):
            return self.text

        class Meta:
            verbose_name = _('Article tag')
            verbose_name_plural = _('Article tags')


class Article(models.Model):

    if config.IS_ARTICLE_TYPE_ENABLED:
        type = models.ForeignKey(
            ArticleType, verbose_name=_('Type'), blank=True, null=True,
            related_name='articles', on_delete=models.SET_NULL)

    title = models.CharField(_('Title'), max_length=255)

    logo = models.ImageField(
        blank=True, null=True, upload_to='article_logos')

    description = models.CharField(_('Description'), max_length=255)

    text = RichTextUploadingField(_('Text'), max_length=50000)

    created = models.DateTimeField(_('Created'), db_index=True)

    author = models.CharField(_('Author'), max_length=255, blank=True)

    if config.ARE_COMMENTS_ENABLED:
        are_comments_enabled = models.BooleanField(
            _('Are comments enabled'), default=True)

    if config.ARE_TAGS_ENABLED:
        tags = models.ManyToManyField(
            ArticleTag,
            verbose_name=_("Tags"),
            related_name='tags',
            blank=True)

    @classmethod
    def most_popular(cls, article_type):

        ct = ContentType.objects.get_for_model(cls)

        hitcount = apps.get_model('hitcount', 'HitCount')

        ids = hitcount.objects.filter(content_type=ct).order_by('-hits')\
            .values_list('object_pk', flat=True)

        return cls.objects.filter(
            type__slug=article_type,
            id__in=ids
        ).extra(
            select={
                'manual': 'FIELD(articles_article.id,%s)' %
                          ','.join(map(str, ids))
            },
            order_by=['manual']
        )

    @classmethod
    def get_related_articles(cls, article_type, exclude_pk, count=6):

        index = 0

        related_articles = cls.objects.filter(
            type__slug=article_type
        ).exclude(
            pk=exclude_pk
        )

        related_articles_count = len(related_articles)

        if related_articles_count:

            if related_articles_count > count:
                index = randint(0, related_articles_count - count)

            return related_articles[index:index + count]

        return []

    @cached_property
    def related_articles(self):
        return self.get_related_articles(self.type.slug, self.pk)

    @property
    def hits(self):
        hitcount = apps.get_model('hitcount', 'HitCount')
        return hitcount.objects.get_for_object(self).hits

    @property
    def slug(self):
        return slugify_url(self.title, separator='_')

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        params = {'slug': self.slug, 'id': self.pk}

        if config.IS_ARTICLE_TYPE_ENABLED:
            params['type'] = self.type.slug

        return reverse_lazy('articles:info', kwargs=params)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ['-created']
