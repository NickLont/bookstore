from django import forms


class quantityChange(forms.Form):
    quantity_input = forms.IntegerField(label='New value', min_value=0)