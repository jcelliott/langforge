from django import forms

class NewLanguageForm(forms.Form):
    name = forms.CharField(max_length=100)

class LanguageInfoForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    info = forms.CharField(required=False, widget=forms.Textarea)

class PhoneticsForm(forms.Form):
    syllable_template = forms.CharField(max_length=100, required=False)
    word_template = forms.CharField(max_length=100, required=False)

class NewSoundForm(forms.Form):
    character = forms.CharField(max_length=3)

class NewClassForm(forms.Form):
    description = forms.CharField(max_length=100)
    abbreviation = forms.CharField(max_length=1)
