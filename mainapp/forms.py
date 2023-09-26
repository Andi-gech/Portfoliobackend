from django import forms
from .models import About, Blog, Projects, Skills, SocialLinks, userfeedback
from django.contrib import admin

class AboutAdminForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

    def clean(self):
        if About.objects.exists():
            raise forms.ValidationError("About already exists")
        return self.cleaned_data