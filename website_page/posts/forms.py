from django import forms
from .models import Post
class ImageForm(forms.ModelForm):
     """Form for the image model"""
     class Meta:
         model = Post
         fields = ('title','slug','intro','body', 'image')
