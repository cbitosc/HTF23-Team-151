from django import forms
from events.models import clubevents

class paperform(forms.ModelForm):
    class Meta :
            model=clubevents
            fields="__all__"