===============
PWD Front Admin
===============

Django-front Admin is a simple Django app to administrate pages from ```Django-PWD-front```
package.

Installation
------------

1. Add ``pwd_front_admin`` to your ``INSTALLED_APPS`` setting like this: ::

    INSTALLED_APPS = [
	...
	'pwd_front_admin',
    ]

2. Include the front URLconf as root pages in your project urls.py like this: ::

    path('', include('pwd_front_admin.urls', namespace='front_admin')),

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


