from django.contrib import admin
from .  models import *

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class MyUserAdmin(BaseUserAdmin):
    list_display=('username', 'email', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username', 'password1', 'password2'),
        }),
    )

    ordering=('email',)
    

# Register your models here.
admin.site.register(MyStudents, MyUserAdmin)
admin.site.register(MyStaff, MyUserAdmin)
admin.site.register(Patient)
admin.site.register(Patientinfo)
admin.site.register(Clinics)
admin.site.register(History)
admin.site.register(General)
admin.site.register(Family)
admin.site.register(Management)
admin.site.register(Medication)
admin.site.register(Diagnosis)
admin.site.register(OD)
admin.site.register(OS)
admin.site.register(Investigation)
admin.site.register(RE)
admin.site.register(LE)
admin.site.register(Visual)
admin.site.register(IOPA)
admin.site.register(IOPB)

admin.site.register(EYELIDR)
admin.site.register(EYELIDL)
admin.site.register(CONJUNCTIVAR)
admin.site.register(CONJUNCTIVAL)
admin.site.register(CORNEAR)
admin.site.register(CORNEAL)
admin.site.register(ACR)
admin.site.register(ACL)
admin.site.register(PUPILR)
admin.site.register(PUPILL)
admin.site.register(IRISR)
admin.site.register(IRISL)
admin.site.register(LENSR)
admin.site.register(LENSL)
admin.site.register(VITREOUSR)
admin.site.register(VITREOUSL)
admin.site.register(RETINAR)
admin.site.register(RETINAL)
admin.site.register(StaffContactinfo)
