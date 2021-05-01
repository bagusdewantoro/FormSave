from django.shortcuts import render, redirect
from .models import Cost
from .forms import CostForm
from django.urls import reverse

def costView(request):
    costResult = Cost.objects.all().last()
    biggestCost = Cost.objects.all().order_by('-costModel').first()

    if request.method == 'POST':
        form = CostForm(request.POST)
        if form.is_valid():
            setDate = request.POST.get('dateValue')
            setCost = request.POST.get('costValue')
            newData = Cost(dateModel=setDate, costModel=setCost)
            newData.save()
            return redirect(reverse('cost'))
    else:
        form = CostForm()
    return render(request, 'jobs/cost.html', {'form':form, 'lastData':costResult,
                                            'biggest':biggestCost})
