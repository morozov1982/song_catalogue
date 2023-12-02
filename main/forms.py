from django import forms
from django.contrib.postgres.forms import SimpleArrayField

from .models import Song


class SongForm(forms.ModelForm):
    links = forms.URLField(widget=forms.Textarea(attrs={'rows': 3}), help_text='Введите каждую ссылку с новой строки')
    performer_order = SimpleArrayField(forms.IntegerField(), required=False)

    class Meta:
        model = Song
        fields = '__all__'
