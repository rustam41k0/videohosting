from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'text'


class UploadVideoForm(forms.Form):
    title = forms.CharField(label='Название', max_length=20,
                            widget=forms.TextInput(attrs={'placeholder': 'Название'}), required=True)
    preview = forms.ImageField(label='Превью', required=True)
    video = forms.FileField(label='Видео', required=True)
    description = forms.CharField(label='Описание', max_length=300,
                                  widget=forms.TextInput(attrs={'placeholder': 'Описание'}), required=True)


class LikeForm(forms.Form):
    video_id = forms.IntegerField(widget=forms.HiddenInput())


class DislikeForm(forms.Form):
    video_id = forms.IntegerField(widget=forms.HiddenInput())