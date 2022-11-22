from django.forms import ModelForm
from django import forms

from .models import *

from django.forms import ModelForm


class UploadForm(ModelForm):
    message = forms.FileField(label="Upload transcription document [ONLY PDF FORMAT]")
    file = forms.FileField(label="Upload audio file")

    class Meta:
        model = Audio
        fields = ['name', 'file','message']

