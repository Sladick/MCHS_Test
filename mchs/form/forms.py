from django import forms
from .models import Test, People, PlanRemoval
from django.forms.formsets import formset_factory


from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'


TestFormset = formset_factory(TestForm)


class PlanRemovalForm(forms.Form):
    plan = forms.FileField()
    number = TestFormset()



class PeopleForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField()
    test_number = TestFormset()
