from django import forms
from .models import Community

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Community.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("A community with this name already exists.")
        return name