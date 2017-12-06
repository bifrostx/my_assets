from django import forms
from my_coin.models import Token


class TokenForm(forms.ModelForm):
    name = forms.CharField(max_length=10)
    amount = forms.DecimalField(max_digits=10, decimal_places=3)
    # price = forms.DecimalField(max_digits=10, decimal_places=3, widget=forms.HiddenInput())
    # balance = forms.DecimalField(max_digits=10, decimal_places=3, widget=forms.HiddenInput())

    class Meta:
        model = Token
        fields = ('name','amount')
