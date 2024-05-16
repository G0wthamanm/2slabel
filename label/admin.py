from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Label
# from .models import Comment
class LabelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  list_display = ( "id","user","supplierlabel","wistronlabel","s_trace","w_trace","s_quantity","w_quantity","s_id","w_id","s_name","w_name","created","error_code","status") 
  search_fields = ['supplierlabel','wistronlabel']
  pass 

admin.site.register(Label,LabelAdmin)
# admin.site.register(Comment)