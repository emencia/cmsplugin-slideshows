.. _Django: https://www.djangoproject.com/
.. _DjangoCMS: http://www.django-cms.org/
.. _emencia-django-slideshows: https://github.com/emencia/emencia-django-slideshows

====================
cmsplugin_slideshows
====================

emencia-django-slideshows plugins for DjangoCMS

Links
*****

* Download his `PyPi package <https://pypi.python.org/pypi/cmsplugin-slideshows>`_;
* Clone it on his `repository <https://github.com/emencia/cmsplugin-slideshows>`_;

Requires
********

* Django >= 1.7;
* `DjangoCMS`_ >= 3.1;
* `emencia-django-slideshows`_ >= 1.0.0;

Install
*******

First install the package (will install `emencia-django-slideshows`_ if not already did) ::

    pip install cmsplugin-slideshows

Enable in your installed Django apps in settings: ::

    INSTALLED_APPS = (
        ...
        'slideshows',
        'cmsplugin_slideshows',
        ...
    )

Then import `emencia-django-slideshows`_ settings: ::

    from porticus.settings import *

Finally install app models in your database using Django migrations: ::

    python manage.py migrate

Usage
*****

Once installed, slideshow contents will be available from content plugins and also in the CMS toolbar.

Just go to the pages and use the plugin in a placeholder content. You will have to select a Slideshow that will be used in your page.

There is actually two content plugins:

Slides show
    The default one to display your slides in a slideshow, it use the template defined in the slideshow object (or the default template if empty);
Random slide
    To display only one random slide.
    
    It will never use the template defined in the slideshow object, instead it will use the template ``slideshows/random_slide/default.html``. Unlike the *Slides show* plugin it don't embed a javascript config template because this is not really useful for a simple slide;

