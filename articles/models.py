
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy

from ckeditor_uploader.fields import RichTextUploadingField

from articles.settings import DEFAULT_ARTICLE_TYPE, ARTICLE_TYPE_CHOICES


class Article(models.Model):

    type = models.CharField(
        _('Type'), choices=ARTICLE_TYPE_CHOICES, default=DEFAULT_ARTICLE_TYPE,
        max_length=255)

    title = models.CharField(_('Title'), max_length=255)

    logo = models.ImageField(
        blank=True, null=True, upload_to='article_logos')

    description = models.CharField(_('Description'), max_length=255)

    text = RichTextUploadingField(_('Text'), max_length=10000)

    created = models.DateTimeField(_('Created'), db_index=True)

    author = models.CharField(_('Author'), max_length=255, blank=True)

    is_comments_enabled = models.BooleanField(
        _('Is comments enabled'), default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('articles:info', kwargs={
            'article_type': self.type,
            'article_id': self.pk
        })

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ['-created']
