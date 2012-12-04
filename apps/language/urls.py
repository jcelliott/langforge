from django.conf.urls.defaults import *

urlpatterns = patterns('language.views',
    url(r'^all/$', 'all_languages', name="language_all_languages"),
    url(r'^$', 'user_languages', name="language_user_languages"),
    url(r'^(?P<id>\d+)/$', 'language', name="language_language"),
    url(r'^new/$', 'new_language', name="language_new_language"),
    # url(r'^forge/(?P<id>\d+)/$', 'forge_language', name="language_forge_language"),
)
