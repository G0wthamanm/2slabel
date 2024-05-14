from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class UserAddForm(UserCreationForm):
	'''
	Extending UserCreationForm - with email

	'''
	

	class Meta:
		model = User
		fields = ['username','password1','password2']
		

	def clean_email(self):
		email = self.cleaned_data['email']
		qry = User.objects.filter(email = email)

		domain_list = ['Wistron.com','wistron.com','whqwistron.com']
		get_wistron_domain = email.split('@')[1]#get me whatever after @, eg. wistron.com

		print(get_wistron_domain in domain_list)

		if qry.exists():
			'''
			True - Queryset exist run validation message here
			'''
			raise forms.ValidationError('email {0} already exists'.format(email))


		elif get_wistron_domain not in domain_list:
			print('test - not in domain')
			raise forms.ValidationError('email does not contain domain')

		return email






class UserLogin(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))


