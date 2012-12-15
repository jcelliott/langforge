from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.CharField("langugage name", max_length=100)
    daughter = models.OneToOneField('Language', blank=True, null=True)
    parent = models.ForeignKey('Language', related_name='daughter_languages', blank=True, null=True)
    creator = models.ForeignKey(User)
    popularity = models.IntegerField()
    info = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Phonetics(models.Model):
    syllable_template = models.CharField(max_length=100)
    word_template = models.CharField(max_length=100)
    # language = models.ForeignKey(Language)
    language = models.OneToOneField(Language)

    def __unicode__(self):
        return ("%s:phonetics" % (self.language.name))

# sound class
class Class(models.Model):
    description = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=1)

    def __unicode__(self):
        return ("%s (%s)" % (self.description, self.abbreviation))

class Sound(models.Model):
    character = models.CharField(max_length=1)
    classes = models.ManyToManyField(Class, blank=True, null=True)
    phonetics = models.ForeignKey(Phonetics)

    def __unicode__(self):
        return self.character

