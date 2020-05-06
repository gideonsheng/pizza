from django import forms
from .models import Pizza,Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['text']
        lables = {'text':''}


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['text']
        lables = {'text':' '}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}