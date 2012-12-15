from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from language.models import *
from language.forms import *

import logging

logger = logging.getLogger(__name__)

# url(r'^all/$', all_languages, name="language_all_languages"),
# url(r'^$', user_languages, name="language_user_languages"),
# url(r'^(?P<id>\d+)/$', language, name="language_language"),
# url(r'^new/$', new_language, name="language_new_language"),
# url(r'^forge/(?P<id>\d+)/$', forge_language, name="language_forge_language"),

def all_languages(request):
    languages = Language.objects.all()
    return render_to_response('language/languages.html', {'languages':languages}, RequestContext(request))

@login_required
def user_languages(request):
    languages = Language.objects.filter(creator=request.user.id)
    return render_to_response('language/forge.html', {'languages':languages}, RequestContext(request))

def language(request, id):
    try:
        language = Language.objects.get(pk=id)
    except Language.DoesNotExist:
        raise Http404
    context = {'language':language,
               'is_owner':False}
    if language.creator.id == request.user.id:
        context['is_owner'] = True
    try:
        context['phonetics'] = language.phonetics
    except Phonetics.DoesNotExist:
        pass
    try:
        context['sounds'] = language.phonetics.sound_set.all()
    except Phonetics.DoesNotExist:
        pass

    return render_to_response('language/language.html', context, RequestContext(request))

@login_required
def new_language(request):
    if request.method == 'POST':
        form = NewLanguageForm(request.POST)
        if not form.is_valid():
            return render_to_response('language/edit.html',
                                      {'form':form},
                                      context_instance=RequestContext(request))

        l = Language()
        l.name = form.cleaned_data['name']
        l.creator = request.user
        l.popularity = 1
        l.save()
        return HttpResponseRedirect(reverse('language.views.user_languages'))

    else:
        form = NewLanguageForm()
        return render_to_response('language/edit.html',
                                  {'form':form},
                                  context_instance=RequestContext(request))

@login_required
def delete(request, id):
    try:
        language = Language.objects.get(pk=id)
    except Language.DoesNotExist:
        raise Http404
    if language.creator.id != request.user.id:
        raise Http404

    language.delete()
    return HttpResponseRedirect(reverse('language.views.user_languages'))

@login_required
def edit_info(request, id):
    try:
        language = Language.objects.get(pk=id)
    except Language.DoesNotExist:
        raise Http404
    if language.creator.id != request.user.id:
        raise Http404

    if request.method == 'POST':
        form = LanguageInfoForm(request.POST)
        if not form.is_valid():
            return render_to_response('language/edit.html',
                                      {'form':form},
                                      RequestContext(request))

        language.name = form.cleaned_data['name']
        language.info = form.cleaned_data['info']
        language.save()
        return redirect('language.views.language', id=language.id)

    else:
        form = LanguageInfoForm(
            initial={'name':language.name, 'info':language.info}
        )
        return render_to_response('language/edit.html',
                                  {'form':form},
                                  RequestContext(request))

@login_required
def edit_phonetics(request, id):
    try:
        language = Language.objects.get(pk=id)
    except Language.DoesNotExist:
        raise Http404
    phonetics = None
    try:
        phonetics = language.phonetics
    except Phonetics.DoesNotExist:
        pass
    if language.creator.id != request.user.id:
        raise Http404

    if request.method == 'POST':
        form = PhoneticsForm(request.POST)
        if not form.is_valid():
            return render_to_response('language/edit.html',
                                      {'form':form},
                                      RequestContext(request))

        if phonetics is None:
            phonetics = Phonetics()
            phonetics.language = language
        phonetics.syllable_template = form.cleaned_data['syllable_template']
        phonetics.word_template = form.cleaned_data['word_template']
        phonetics.save()
        return redirect('language.views.language', id=language.id)

    else:
        if phonetics is None:
            form = PhoneticsForm()
        else:
            form = PhoneticsForm(
                initial={'syllable_template':phonetics.syllable_template, 'word_template':phonetics.word_template}
            )
        return render_to_response('language/edit.html',
                                  {'form':form},
                                  RequestContext(request))

@login_required
def add_sound(request, id):
    if request.method == 'POST':
        form = NewSoundForm(request.POST)
        if not form.is_valid():
            return render_to_response('language/edit.html',
                                      {'form':form},
                                      context_instance = RequestContext(request))

        try:
            language = Language.objects.get(pk=id)
        except Language.DoesNotExist:
            raise Http404
        try:
            phonetics = language.phonetics
        except Phonetics.DoesNotExist:
            raise Http404
        if language.creator.id != request.user.id:
            raise Http404

        sound = Sound()
        sound.phonetics = phonetics
        sound.character = form.cleaned_data['character']
        sound.save()
        return redirect('language.views.language', id=language.id)

    else:
        form = NewSoundForm()
        return render_to_response('language/edit.html',
                                  {'form':form},
                                  context_instance = RequestContext(request))

@login_required
def remove_sound(request, id, sound_id):
    # logger = logging.getLogger(__name__)
    try:
        language = Language.objects.get(pk=id)
    except Language.DoesNotExist:
        raise Http404
    if language.creator.id != request.user.id:
        raise Http404
    try:
        sound = Sound.objects.get(pk=sound_id)
    except Sound.DoesNotExist:
        raise Http404

    sound.delete()
    return redirect('language.views.language', id=language.id)

