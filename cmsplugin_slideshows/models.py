# -*- coding: utf-8 -*-
"""
Models for plugin contents
"""
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from slideshows.models import DEFAULT_SLIDESHOWS_TEMPLATE, DEFAULT_SLIDESHOWS_RANDOM_SLIDE_TEMPLATE

from cms.models.pluginmodel import CMSPlugin

class SlideshowPlugin(CMSPlugin):
    slideshow = models.ForeignKey('slideshows.Slideshow')
    template = models.CharField(_('content template'), choices=settings.SLIDESHOWS_TEMPLATES, default=DEFAULT_SLIDESHOWS_TEMPLATE, max_length=100, blank=False)

    def __unicode__(self):
        return self.slideshow.title

class SlideshowRandomImagePlugin(CMSPlugin):
    slideshow = models.ForeignKey('slideshows.Slideshow')
    template = models.CharField(_('content template'), choices=settings.SLIDESHOWS_RANDOM_SLIDE_TEMPLATES, default=DEFAULT_SLIDESHOWS_RANDOM_SLIDE_TEMPLATE, max_length=100, blank=False)

    def __unicode__(self):
        return self.slideshow.title
