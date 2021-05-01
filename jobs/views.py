from django.shortcuts import render, redirect
from .models import Cost
from .forms import CostForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def costView(request):
    costResult = Cost.objects.all().last()
    if request.method == 'POST':
        form = CostForm(request.POST)

        if form.is_valid():
            date = request.POST.get('date', '')
            cost = request.POST.get('cost', '')
            cost_obj = Cost(dateModel=date, costModel=cost)
            cost_obj.save()
            return HttpResponseRedirect(reverse('cost'))
    else:
        form = CostForm()
    return render(request, 'jobs/cost.html',
            {'form':form, 'costhtml':costResult})
