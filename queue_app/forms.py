from django import forms
from .models import *


class OperatorsForm(forms.ModelForm):
    class Meta:
        model = QueueTab
        fields = ['ticket', 'id']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = QueueTab
        # labels = ['ticket']
        fields = ['ticket']
        widgets = {'ticket': forms.HiddenInput()}


