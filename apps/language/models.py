from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.CharField("langugage name", max_length=256)
    daughter = models.OneToOneField('Language')
    parent = models.ForeignKey('Language', related_name='daughter_languages')
    creator = models.ForeignKey(User)
    popularity = models.IntegerField()

class Phonetics(models.Model):
    syllable_template = models.CharField(max_length=256)
    word_template = models.CharField(max_length=256)

# sound class
class Class(models.Model):
    description = models.CharField(max_length=256)
    abbreviation = models.CharField(max_length=1)

class Sound(models.Model):
    character = models.CharField(max_length=1)
    classes = models.ManyToManyField(Class)

