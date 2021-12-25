from django.contrib import admin

# Register your models here.
from .models import MAINpageContent

class MpCAdmin(admin.ModelAdmin):
    list_display = ( "Heading1","Heading2" ,"buttonHeading" ,"intro_pic" )


admin.site.register(MAINpageContent, MpCAdmin)