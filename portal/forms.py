from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from portal.models import Emmamodel, Christymodel, Robmodel, Imomodel


class Emmaform(forms.ModelForm):
    class Meta:
        model = Emmamodel
        fields = '__all__'


class Christyform(forms.ModelForm):
    class Meta:
        model = Christymodel
        fields = '__all__'


class Robform(forms.ModelForm):
    class Meta:
        model = Robmodel
        fields = '__all__'


class Imoform(forms.ModelForm):
    class Meta:
        model = Imomodel
        fields = '__all__'
