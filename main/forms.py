from django.forms import ModelForm
from .models import Player


class PlayerForm(ModelForm):

    class Meta:
        model = Player
        fields = ('name',)


class CommentForm(ModelForm):

    class Meta:
        model = Player
        fields = ('comment',)
