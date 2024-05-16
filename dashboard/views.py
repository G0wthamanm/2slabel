from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q
import datetime 
import email
from datetime import date
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse
from label.models import Label
from accounts.forms import UserAddForm
from label.forms import LabelCreationForm
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import time
from django.http import JsonResponse
# from label.forms import CommentForm






def label_creation(request):
	if not request.user.is_authenticated:
		return redirect('accounts:login')
	if request.method == 'POST':
		form = LabelCreationForm(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			user = request.user
			instance.user = user
			employee_email=instance.user.email
			instance.save()
			time.sleep(5)
			return redirect("dashboard:createlabel")
	else:
		dataset = dict()
		form = LabelCreationForm()
		dataset['form'] = form
		dataset['title'] = 'Label Verification'
		return render(request,'dashboard/create_label.html',dataset)
	# return HttpResponse('label creation form')



 

def labels_list(request):
	if not (request.user.is_staff and request.user.is_superuser):
		return redirect('/')
	labels = Label.objects.all_pending_labels()
	#labels = Label.objects.filter(created=date.today())
	#time.sleep(3)
	return render(request,'dashboard/labels_recent.html',{'label_list':labels,'title':'labels list - pending'})



def labels_approved_list(request):
	if not (request.user.is_superuser and request.user.is_staff):
		return redirect('/')
	labels = Label.objects.all_approved_labels() #approved labels -> calling model manager method
	return render(request,'dashboard/labels_approved.html',{'label_list':labels,'title':'approved label list'})



def labels_view(request,id):
	if not (request.user.is_authenticated):
		return redirect('/')

	label = get_object_or_404(Label, id = id)
	
	return render(request,'dashboard/label_detail_view.html',{'label':label,'title':'{0}-{1} label'.format(label.user.username,label.status)})






def view_my_label_table(request):
	# work on the logics
	if request.user.is_authenticated:
		user = request.user
		labels = Label.objects.filter(user = user)
		print(labels)
		dataset = dict()
		dataset['label_list'] = labels
	
		dataset['title'] = 'Labels List'
	else:
		return redirect('accounts:login')
	return render(request,'dashboard/staff_labels_table.html',dataset)





