from setuptools import setup, find_packages

setup(
    name='cmsplugin-slideshows',
    version=__import__('cmsplugin_slideshows').__version__,
    description=__import__('cmsplugin_slideshows').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='dthenon@emencia.com',
    url='https://github.com/emencia/cmsplugin-slideshows',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        "Framework :: Django :: 1.4",
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'Django>=1.7',
        'django-cms>=3.1',
        'emencia-django-slideshows>=1.0.0',
    ],
    include_package_data=True,
    zip_safe=False
)