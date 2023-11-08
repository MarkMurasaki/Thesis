from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(label='Amount')
    id = forms.CharField(label='Source ID')
    description = forms.CharField(label='Description', initial='GCash Payment Description')
