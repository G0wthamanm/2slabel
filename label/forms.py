from django import forms
from django.conf import settings
from django.forms import DateField
from .models import Label
# from .models import Comment
import datetime

class LabelCreationForm(forms.ModelForm):
	#created=DateField(input_formats=settings.DATE_INPUT_FORMATS)
	class Meta:
		model = Label
		exclude = ['user','updated','created']








# class CommentForm(forms.ModelForm):

# 	class Meta:
# 		model = Comment
# 		exclude = ['updated','created','label']