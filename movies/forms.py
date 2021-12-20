from django import forms
from django.db.models import fields
from .models import Raiting, RaitingStar, Review

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name','email', 'Text']
    
    def save(self, commit=False):
        super().save(commit=commit)


# Не використовується, там шось треба робити в js і я  покішо хз як це зробити
class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(queryset=RaitingStar.objects.all(), widget=forms.RadioSelect(), empty_label='star')
    class Meta:
        model = Raiting
        fields = ['star']
