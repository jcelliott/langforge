langforge
=========

###installation###

    pip install virtualenv (or install it with your package manager, it will probably be called python-virtualenv)
    virtualenv langforge-env
    cd langforge-env
    source bin/activate
    pip install pinax
    vim lib/python2.7/site-packages/pinax/core/management/commands/setup_project.py +207
change `pip.call_subprocess` to `pip.util.call_subprocess` to fix [a bug](http://stackoverflow.com/questions/12250317/python-pinax-django-windows-attributeerror-module-object-has-no-attribute)

    pinax-admin setup_project -b basic temp
    rm -rf temp
    git clone git://github.com/joshuacelliott/langforge.git
    cd langforge
    python manage.py runserver
