from django.db import models
import datetime

class LabelManager(models.Manager):
	def get_queryset(self):
		'''
		overrides objects.all() 
		return all labels including pending or approved
		'''
		return super().get_queryset()



	def all_pending_labels(self):
		'''
		gets all pending labels -> Label.objects.all_pending_labels()
		'''
		return super().get_queryset().order_by('-created')# applying FIFO 






