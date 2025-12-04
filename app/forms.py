from django import forms
from app.models import employe_model
class employe_form(forms.ModelForm):
    class Meta:
        model = employe_model
        fields = '__all__'