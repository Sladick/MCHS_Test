
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *




class Post(CreateView):
    template_name = 'form/index.html'
    Test_form = TestForm()
    PlanRemoval_form = PlanRemovalForm()
    People_form = PeopleForm()

    def get(self, request, *args, **kwargs):
        context = {'test': self.Test_form, 'plan_removal': self.PlanRemoval_form, 'people': self.People_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {'test': self.Test_form, 'plan_removal': self.PlanRemoval_form, 'people': self.People_form}
        Test_form = TestForm(request.POST)
        PlanRemoval_form = PlanRemovalForm(request.POST)
        People_form = PeopleForm(request.POST)
        if Test_form.is_valid() and PlanRemoval_form.is_valid() and People_form.is_valid():
            per_f = Test_form.save()
            ph_f = PlanRemoval_form.save(commit=False)
            ph_f.number_id = per_f.id
            ph_f.save()
            ph_j = People_form.save(commit=False)
            ph_j.test_number_id = per_f.id
            ph_j.save()
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)


