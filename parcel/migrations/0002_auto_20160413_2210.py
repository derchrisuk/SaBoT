# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='originText',
            field=models.CharField(max_length=256, verbose_name='Name or description of the sender if it is no registered owner', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parcel',
            name='ownerId',
            field=models.PositiveIntegerField(null=True, verbose_name='Key of the owner object', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parcel',
            name='ownerType',
            field=models.ForeignKey(verbose_name='Type of the owner object', blank=True, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
    ]
