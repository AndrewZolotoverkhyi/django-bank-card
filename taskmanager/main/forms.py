from django import forms


class UserForm(forms.Form):
    cardNumber = forms.CharField(label='Card Number', required=True, min_length=14, max_length=16)
    password = forms.CharField(widget=forms.PasswordInput(), label='PIN', required=True, min_length=4, max_length=4)
