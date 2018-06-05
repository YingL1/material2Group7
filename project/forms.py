from django.contrib.auth.forms import UserCreationForm
from .models import User,Device,Component, DeviceModel
from django import forms

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

class DeviceForm(forms.Form):
	device_model = forms.ModelChoiceField(queryset=DeviceModel.objects.all())
	components = Component.objects.all()
	component_working = forms.ModelMultipleChoiceField(components, widget=forms.CheckboxSelectMultiple())
	component_not_working = forms.ModelMultipleChoiceField(components, widget=forms.CheckboxSelectMultiple())
    
