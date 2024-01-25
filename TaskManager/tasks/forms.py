import re

from django import forms
from django.core.exceptions import ValidationError
from django.forms import CharField, Textarea

from .models import Task


def capitalized_validator(value):
  if value[0].islower():
    raise ValidationError('Value must be capitalized.')


class TaskForm(forms.ModelForm):
    title = CharField(validators=[capitalized_validator])
    class Meta:
        model = Task
        # wybieramy pola jakie chcemy użyć
        fields = ('title','desc','importance')
        # albo tych które nie chcemy
        # exclude = ('createDate','completeDate','user')
        # kiedy chcemy wszystkie atrybuty
        # fields = '__all__'

    def clean_desc(self):
        # Force each sentence of the description to be capitalized.
        initial = self.cleaned_data['desc']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)