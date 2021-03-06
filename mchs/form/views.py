from django.shortcuts import render

from .forms import *
from .models import *


def post(request):
    if request.method == 'POST':
        form = TestForm(request.POST)

        plan_instances = PlanFormset(request.POST)
        people_instances = PeopleFormset(request.POST)

        if form.is_valid():
            if plan_instances.is_valid() and people_instances.is_valid():
                print('!!!!', plan_instances)

                team = Test(title=form.cleaned_data['title'], rating=form.cleaned_data['rating'], limitations=form.cleaned_data['limitations'])
                team.save()
                args = {'form': form}
                for item in people_instances:
                    if item.is_valid():
                        x = item.save()
                        team.many_people.add(x)
                    else:
                        print('-----------error occur')
                for item in plan_instances:
                    if item.is_valid():
                        x = item.save()
                        team.many_plan.add(x)
                    else:
                        print('-----------error occur')
                team.save()
                return render(request, 'form/index2.html', args)

        args = {'form': form}
        return render(request, 'form/index2.html', args)
    else:
        form = TestForm()
        args = {'form': form}
        return render(request, 'form/index2.html', args)