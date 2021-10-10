from .models import Test, People, PlanRemoval
from django.forms import ModelForm


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ('title', 'rating', 'limitations')


class PlanRemovalForm(ModelForm):
    class Meta:
        model = PlanRemoval
        fields = ('plan',)


class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ('name', 'last_name', 'patronymic')