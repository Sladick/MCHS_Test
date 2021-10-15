from django import forms
from django.forms.formsets import formset_factory
from .models import *


class TeamForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'


PlanFormset = formset_factory(TeamForm)
PeopleFormset = formset_factory(PeopleForm)


class TestForm(forms.Form):
    title = forms.CharField()
    rating = forms.FloatField()
    limitations = forms.CharField()
    many_team = PlanFormset()
    many_people = PeopleFormset()





