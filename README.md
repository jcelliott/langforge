langforge
=========

###installation###

    virtualenv langforge-env
    cd langforge-env
    source bin/activate
    pip install pinax
    vim lib/python2.7/site-packages/pinax/core/management/commands/setup_project.py +207
change `pip.call_subprocess` to `pip.util.call_subprocess`
    pinax-admin setup_project -b basic temp
    rm -rf temp
    git clone <this repository>
    cd langforge
    python manage.py runserver