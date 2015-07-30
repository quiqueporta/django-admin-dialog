# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers
from django.db import models

DEFAULT_WIDTH = 300
DEFAULT_MAX_HEIGHT = 600


class DjangoAdminDialog(models.Model):

    class Meta:
        verbose_name = 'DjangoAdminDialog'
        verbose_name_plural = 'DjangoAdminDialogs'
        unique_together = ('url', 'element_id',)

    url = models.CharField(max_length=255, blank=False, null=False)
    element_id = models.CharField(max_length=255, blank=False, null=False)
    title = models.CharField(max_length=255, blank=True, null=False)
    body = models.TextField(blank=False, null=False)
    active = models.BooleanField(blank=True, null=False, default=True)
    width = models.SmallIntegerField(blank=True, null=False, default=DEFAULT_WIDTH)
    max_height = models.SmallIntegerField(blank=True, null=False, default=DEFAULT_MAX_HEIGHT)

    def __unicode__(self):
        return "{} for {}".format(self.element_id, self.url)

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))