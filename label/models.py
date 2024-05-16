from unittest.util import _MAX_LENGTH
from django.db import models
from sqlalchemy import null
from .manager import LabelManager
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone



class Label(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	#email = models.EmailField()
	supplierlabel=models.CharField(max_length=100,null=True,blank=True)
	s_trace=models.CharField(max_length=100,null=True,blank=True)
	s_quantity=models.CharField(max_length=100,null=True,blank=True)
	s_id=models.CharField(max_length=100,null=True,blank=True)
	s_name= models.CharField(max_length=100,null=True,blank=True)
	wistronlabel=models.CharField(max_length=100,null=True,blank=True)
	w_trace=models.CharField(max_length=100,null=True,blank=True)
	w_quantity=models.CharField(max_length=100,null=True,blank=True)
	w_id= models.CharField(max_length=100,null=True,blank=True)
	w_name= models.CharField(max_length=100,null=True,blank=True)
	#updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False,auto_now_add=True)
    

	objects = LabelManager()


	class Meta:
		verbose_name = _('Label')
		verbose_name_plural = _('Labels')
		ordering = ['-created'] #recent objects



	


	@property
	def pretty_label(self):
		'''
		i don't like the __str__ of label object - this is a pretty one :-)
		'''
		label = self.labeltype
		user = self.user
		employee = user.employee_set.first().get_full_name
		return ('{0} - {1}'.format(employee,label))


	def error_code(self):
		supplierlabel = self.supplierlabel
		wistronlabel = self.wistronlabel
		s_trace = self.s_trace
		w_trace = self.w_trace
		s_name = self.s_name
		w = self.w_name
		s_qty = self.s_quantity
		w_qty = self.w_quantity
		s_id= self.s_id
		w_id=self.w_id

		if supplierlabel != wistronlabel and s_trace != w_trace and s_name != w and s_qty != w_qty and s_id == w_id :
			return "ID,Trace_ID,QTY,Name &  ID MISMATCH"
		elif  supplierlabel != wistronlabel:
			return "LABEL MISMATCH"
		elif  s_trace != w_trace:
			return "TRACE-ID MISMATCH"
		elif s_name != w:
			return "NAME MISMATCH"
		elif s_qty != w_qty:
			return "QUANTITY MISMATCH"
		else:
			return "NONE"


	@property
	def status(self):
		supplierlabel = self.supplierlabel
		wistronlabel = self.wistronlabel
		s_trace = self.s_trace
		w_trace = self.w_trace
		s_name = self.s_name
		w = self.w_name
		s_qty = self.s_quantity
		w_qty = self.w_quantity
		s_id= self.s_id
		w_id=self.w_id
		if supplierlabel == wistronlabel and s_trace == w_trace and s_name == w and s_qty == w_qty and s_id != w_id:
			return  "PASS"
		elif s_id[0].isdigit():
			return "fail"
		else:
			return "FAIL"





	@property
	def label_approved(self):
		return self.is_approved == True




	@property
	def approve_label(self):
		if not self.is_approved:
			self.is_approved = True
			self.status = 'approved'
			self.save()




	@property
	def unapprove_label(self):
		if self.is_approved:
			self.is_approved = False
			self.status = 'pending'
			self.save()



	@property
	def labels_cancel(self):
		if self.is_approved or not self.is_approved:
			self.is_approved = False
			self.status = 'cancelled'
			self.save()



	# def uncancel_label(self):
	# 	if  self.is_approved or not self.is_approved:
	# 		self.is_approved = False
	# 		self.status = 'pending'
	# 		self.save()



	@property
	def reject_label(self):
		if self.is_approved or not self.is_approved:
			self.is_approved = False
			self.status = 'rejected'
			self.save()



	@property
	def is_rejected(self):
		return self.status == 'rejected'




	# def save(self,*args,**kwargs):
	# 	data = self.defaultdays
	# 	days_left = data - self.label_days
	# 	self.defaultdays = days_left
	# 	super().save(*args,**kwargs)




# class Comment(models.Model):
# 	label = models.ForeignKey(Label,on_delete=models.CASCADE,null=True,blank=True)
# 	comment = models.CharField(max_length=255,null=True,blank=True)

# 	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
# 	created = models.DateTimeField(auto_now=False, auto_now_add=True)


# 	def __str__(self):
# 		return self.label

