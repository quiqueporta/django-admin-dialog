# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from django.conf import settings as django_settings
from .settings import DJANGO_ADMIN_DIALOG_SHOW_IDS
from .models import DjangoAdminDialog


def django_admin_dialog(request):
    results = []

    tooltips = DjangoAdminDialog.objects.filter(active=True)
    for tooltip in tooltips:
        if request.path.startswith(tooltip.url):
            results.append(tooltip)

    django_admin_dialog_show_ids = DJANGO_ADMIN_DIALOG_SHOW_IDS
    if hasattr(django_settings, 'DJANGO_ADMIN_DIALOG_SHOW_IDS'):
        django_admin_dialog_show_ids = django_settings.DJANGO_ADMIN_DIALOG_SHOW_IDS

    return {
        'django_admin_dialogs': results,
        'django_admin_dialog_show_ids': django_admin_dialog_show_ids
    }