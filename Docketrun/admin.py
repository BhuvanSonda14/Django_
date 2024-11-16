from django.contrib import admin

# Register your models here.
from  .models import *

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'age','email')  
         
admin.site.register(Employee,)
admin.site.register(Employee_test)
admin.site.register(Final_trial)