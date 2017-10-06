
from random import randint

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property

from ckeditor_uploader.fields import RichTextUploadingField
from slugify import slugify_url
from hitcount.models import HitCount

from articles.settings import DEFAULT_ARTICLE_TYPE, ARTICLE_TYPE_CHOICES


class Article(models.Model):

    type = models.CharField(
        _('Type'), choices=ARTICLE_TYPE_CHOICES, default=DEFAULT_ARTICLE_TYPE,
        max_length=255)

    title = models.CharField(_('Title'), max_length=255)

    logo = models.ImageField(
        blank=True, null=True, upload_to='article_logos')

    description = models.CharField(_('Description'), max_length=255)

    text = RichTextUploadingField(_('Text'), max_length=50000)

    created = models.DateTimeField(_('Created'), db_index=True)

    author = models.CharField(_('Author'), max_length=255, blank=True)

    is_comments_enabled = models.BooleanField(
        _('Is comments enabled'), default=True)

    @classmethod
    def most_popular(cls, article_type):
        ct = ContentType.objects.get_for_model(cls)
        ids = HitCount.objects.filter(content_type=ct).order_by('-hits')\
            .values_list('object_pk', flat=True)
        return cls.objects.filter(type=article_type, id__in=ids).extra(
            select={'manual': 'FIELD(id,%s)' % ','.join(map(str, ids))},
            order_by=['manual']
        )

    @classmethod
    def get_related_articles(cls, article_type, exclude_pk, count=6):

        index = 0

        related_products = cls.objects.filter(type=article_type).exclude(
            pk=exclude_pk)

        related_products_count = len(related_products)

        if related_products_count:

            if related_products_count > count:
                index = randint(0, related_products_count - count)

            return related_products[index:index + count]

        return []

    @cached_property
    def related_articles(self):
        return self.get_related_articles(self.type, self.pk)

    @property
    def hits(self):
        return HitCount.objects.get_for_object(self).hits

    @property
    def slug(self):
        return slugify_url(self.title, separator='_')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('articles:info', kwargs={
            'type': self.type,
            'slug': self.slug,
            'id': self.pk
        })

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ['-created']
