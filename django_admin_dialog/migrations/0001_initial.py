# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoAdminDialog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=255)),
                ('element_id', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('width', models.SmallIntegerField(default=300, blank=True)),
                ('max_height', models.SmallIntegerField(default=600, blank=True)),
            ],
            options={
                'verbose_name': 'DjangoAdminDialog',
                'verbose_name_plural': 'DjangoAdminDialogs',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='djangoadmindialog',
            unique_together=set([('url', 'element_id')]),
        ),
    ]
