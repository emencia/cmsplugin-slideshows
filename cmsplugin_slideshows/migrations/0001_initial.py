# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slideshows', '0001_initial'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideshowPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'slideshows/slides_show/default.html', max_length=100, verbose_name='content template', choices=[(b'slideshows/slides_show/default.html', b'Slider default'), (b'slideshows/slides_show/royalslider.html', b'Royal slider')])),
                ('slideshow', models.ForeignKey(to='slideshows.Slideshow')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SlideshowRandomImagePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'slideshows/random_slide/default.html', max_length=100, verbose_name='content template', choices=[(b'slideshows/random_slide/default.html', b'Random image default')])),
                ('slideshow', models.ForeignKey(to='slideshows.Slideshow')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
