from django.conf.urls.defaults import *

urlpatterns = patterns('language.views',
    url(r'^all/$', 'all_languages', name="language_all_languages"),
    url(r'^$', 'user_languages', name="language_user_languages"),
    url(r'^(?P<id>\d+)/$', 'language', name="language_language"),
    url(r'^new/$', 'new_language', name="language_new_language"),
    url(r'^delete/(?P<id>\d+)/$', 'delete', name="language_delete"),
    url(r'^edit/(?P<id>\d+)/info/$', 'edit_info', name="language_edit_info"),
    url(r'^edit/(?P<id>\d+)/phonetics/$', 'edit_phonetics', name="language_edit_phonetics"),
    url(r'^edit/(?P<id>\d+)/phonetics/add_sound/$', 'add_sound', name="language_add_sound"),
    url(r'^edit/(?P<id>\d+)/phonetics/remove_sound/(?P<sound_id>\d+)/$', 'remove_sound', name="language_remove_sound")
)
