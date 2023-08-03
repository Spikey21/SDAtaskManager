from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # wybieramy pola jakie chcemy użyć
        fields = ('title','desc','importance')
        # albo tych które nie chcemy
        # exclude = ('createDate','completeDate','user')
        # kiedy chcemy wszystkie atrybuty
        # fields = '__all__'