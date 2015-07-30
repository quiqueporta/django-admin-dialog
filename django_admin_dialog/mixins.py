# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function


class DjangoAdminDialogMixin(object):

    @property
    def media(self):
        media = super(DjangoAdminDialogMixin, self).media

        js = ["django_admin_dialog/js/jquery-ui.js"]
        css = {
            "all": ("django_admin_dialog/css/jquery-ui.css", "django_admin_dialog/css/jquery-ui.structure.css",
                    "django_admin_dialog/css/jquery-ui.theme.css",)
        }

        media.add_js(js)
        media.add_css(css)
        return media