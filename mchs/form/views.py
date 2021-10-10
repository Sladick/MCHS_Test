from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from .forms import *
from .models import *


def post(request):
    if request.method == 'POST':
        form1 = PlanRemovalForm(request.POST)
        form2 = PeopleForm(request.POST)

        test_instances = TestFormset(request.POST)
        if form1.is_valid():
            print("4")
            if form2.is_valid():
                print('5')
                if test_instances.is_valid():
                    plans = PlanRemoval(plam=form1.cleaned_data['plan'])
                    plans.save()
                    peoples = People(name=form2.cleaned_data['name'], last_name=form2.cleaned_data['last_name'], patronymic=form2.cleaned_data['patronymic'])
                    peoples.save()
                    args = {'form1': form1, 'form2': form2, 'form3': test_instances}
                    for item in test_instances:
                        if item.is_valid():
                            tests = item.save()
                            plans.number.add(tests)
                            peoples.test_number.add(tests)
                            print("1")
                        else:
                            print('-----------error occur')
                    plans.save()
                    peoples.save()
                    print("2")
                    return render(request, 'form/index.html', args)
        print("3")

        args = {'form1': form1, 'form2': form2, 'form3': test_instances}
        return render(request, 'form/index.html', args)
    else:
        form1 = PlanRemovalForm()
        form2 = PeopleForm()
        form3 = TestForm()
        args = {'form1': form1, 'form2': form2, 'form3': form3}
        return render(request, 'form/index.html', args)