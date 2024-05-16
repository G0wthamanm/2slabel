from django.urls import path
from .import views


app_name = 'dashboard'

urlpatterns = [

   
    path('verification/',views.label_creation,name='createlabel'),
    path('all/labels/',views.labels_list,name='labelslist'),
    path('label/all/view/<int:id>/',views.labels_view,name='userlabelview'),
    path('users/table/',views.view_my_label_table,name='stafflabeltable'),



]
