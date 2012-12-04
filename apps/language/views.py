from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from language.models import *

# url(r'^all/$', all_languages, name="language_all_languages"),
# url(r'^$', user_languages, name="language_user_languages"),
# url(r'^(?P<id>\d+)/$', language, name="language_language"),
# url(r'^new/$', new_language, name="language_new_language"),
# url(r'^forge/(?P<id>\d+)/$', forge_language, name="language_forge_language"),

def all_languages(request):
    languages = Language.objects.all()
    return render_to_response('language/languages.html', {'languages':languages})

@login_required
def user_languages(request):
    languages = Language.objects.filter(creator=request.user.id)
    return render_to_response('language/languages.html', {'languages':languages})

def language(request, id):
    try:
        lang = Language.objects.get(pk=id)
    except Item.DoesNotExist:
        raise Http404
    return render_to_response('language/lang.html', {'lang':lang})

@login_required
def new_language(request):
    if request.method == 'POST':
        form = NewLanguageForm(request.POST)
        if not form.is_valid():
            return render_to_response('language/new.html',
                                      {'form':form},
                                      context_instance=RequestContext(request))

        l = Language()
        l.user = request.user
        l.name = form.cleaned_data['name']
        l.save()
        return HttpResponseRedirect('language.views.user_languages')

    else:
        form = NewLanguageForm()
        return render_to_response('language/new.html',
                                  {'form':form},
                                  context_instance=RequestContext(request))

# @login_required
# def forge_language(request):

