from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project(models.Model):
    name_text = models.CharField(max_length=200)
    uml_class = models.IntegerField(default=0)
    python_class = models.IntegerField(default=0)
    intersection = models.IntegerField(default=0)
    without_corrections = models.IntegerField(default=0)
    hamming_corrections = models.IntegerField(default=0)
    capital_letters_corrections = models.IntegerField(default=0)
    #pyclass_notuml_list = models.CharField()
    #umlclass_notpy_list = models.CharField()
    #intersection_list = models.CharField()
    def __str__(self):
        return self.name_text
