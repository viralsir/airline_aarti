from django import forms
from .models import course_info
'''class InserForm(forms.Form):
    name=forms.CharField(required=False)
    email=forms.EmailField()
    description=forms.CharField()
    duration=forms.IntegerField(min_value=0)
    fees=forms.IntegerField(min_value=0)
'''

class InserForm(forms.ModelForm):
    class Meta:
        model=course_info
        fields='__all__'
