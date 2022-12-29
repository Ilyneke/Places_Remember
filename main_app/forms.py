from .models import Memory
from django.forms import ModelForm


class MemoryForm(ModelForm):
    class Meta:
        model = Memory
        fields = ['title', 'description', 'author', 'center0', 'center1', 'zoom']
