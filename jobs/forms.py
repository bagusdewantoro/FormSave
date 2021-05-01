from django import forms

class CostForm(forms.Form):
    costValue = forms.DecimalField()
    dateValue = forms.DateField()
