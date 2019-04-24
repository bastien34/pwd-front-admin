===============
PWD Front Admin
===============

Django-front Admin is a simple Django app to administrate pages from ```Django-PWD-front```
package.

The goal of this project is to present a nice layout to handle ```dashboard``` pages. With
this approach in mind which is building a ```dashboard``` application, you'd rather copy
the code in you own project structure than install this app.


Installation
------------

1. Add ``dashboard`` to your ``INSTALLED_APPS`` setting like this: ::

    INSTALLED_APPS = [
	...
	'dashboard',
    ]

2. Include the front URLconf as root pages in your project urls.py like this: ::

    path('', include('dashboard.urls', namespace='front_admin')),

3. This package contains no models, therefore no migrations to do.


4. Add templates directory to your templates: ::

    templates/front/copy_here_your_front_page.html

6. Configure and start coding.


Translation
-----------

1. Make messages: CD in ``front`` directory and run: ::

    $ cd /front

    $ ../test_project/manage.py makemessages -l fr

2. Compile messages, run: ::

    $ ../test_project/manage.py compilemessages


