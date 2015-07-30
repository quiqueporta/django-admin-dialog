# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from django.contrib import admin
from django.db.models.fields import TextField
from redactor.widgets import AdminRedactorEditor

from .models import DjangoAdminDialog


@admin.register(DjangoAdminDialog)
class DjangoAdminDialogAdmin(admin.ModelAdmin):
    formfield_overrides = {
            TextField: {'widget': AdminRedactorEditor},
    }
    list_display = ('url', 'element_id',)
    search_fields = ('url', 'element_id',)
    save_on_top = True
