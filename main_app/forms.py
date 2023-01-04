from .models import Memory
from django.forms import ModelForm, Textarea, TextInput, ModelChoiceField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class MemoryForm(ModelForm):
    class Meta:
        model = Memory
        fields = ['title', 'description', 'author', 'lat', 'lng', 'zoom']
        author = ModelChoiceField(
            queryset=get_user_model().objects.all(),
            to_field_name='username',
            initial=User
        )
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название воспоминания'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание воспоминания'
            }),
            'lat': TextInput(attrs={
                'class': 'form-control',
            }),
            'lng': TextInput(attrs={
                'class': 'form-control',
            }),
            'zoom': TextInput(attrs={
                'class': 'form-control',
            }),
        }
