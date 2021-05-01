from django import forms

class CostForm(forms.Form):
    cost = forms.DecimalField()
    date = forms.DateField()
