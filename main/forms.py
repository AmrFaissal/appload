from django import forms
from .models import App


class AppForm(forms.ModelForm):
	class Meta:
		model = App
		fields = "__all__"
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control'})
		}
	
