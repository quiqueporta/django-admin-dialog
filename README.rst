django-admin-dialog
===================

Shows a dialog popup with helptext for the admin fields that you have indicated.

Requirements
------------

- django-redactoreditor

Installation
------------

Install the app via pip:

.. code-block:: bash

    $ pip install django-admin-dialog

Add `django_admin_dialog` and `redactor` to your installated apps:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'redactor',
        'django_admin_dialog',
        ...

Add the context processor to your `TEMPLATE_CONTEXT_PROCESSORS`:

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'django_admin_dialog.context_processors.django_admin_dialog',
    )

Override the admin base template (`base.html`) and include this:

.. code-block:: html

    {% include "django_admin_dialog/django_admin_dialog.html" %}

In your admin.py file, add this mixin for all your ModelAdmin's that you want to add the dialog:

.. code-block:: python

    from django_admin_dialog.mixins import DjangoAdminDialogMixin

    class MyModelAdmin(DjangoAdminDialogMixin, admin.ModelAdmin):
    ...

And run the migrations:

.. code-block:: bash

    $ manage.py migrate django-admin-dialog

Usage
-----

Access to the DjangoAdminDialog application.

.. image:: https://raw.github.com/quiqueporta/django-admin-dialog/master/app.png

In this form you indicate the url on which you want to show the modal dialog boxes and the field id.

.. image:: https://raw.github.com/quiqueporta/django-admin-dialog/master/admin_form.png

If you want to know the name of the form fields, you can set this setting variable:

.. code-block:: python

    DJANGO_ADMIN_DIALOG_SHOW_IDS = True

Now if you access to your model form, you can see the field id's next to them.

.. image:: https://raw.github.com/quiqueporta/django-admin-dialog/master/field_ids.png


When you access to your model admin form, you can see a new icon next to the field that you indicate previously.

.. image:: https://raw.github.com/quiqueporta/django-admin-dialog/master/help_button.png

And now you can click on this icon to show the dialog.

.. image:: https://raw.github.com/quiqueporta/django-admin-dialog/master/help_dialog.png


