from django.contrib import admin
from .models import *
# Register your models here.

class LoginAdmin(admin.ModelAdmin):
    list_display = ('u_phone',
                    'u_name',
                    'u_ID',
                    'u_company',
                    'u_department1',
                    'u_department2',
                    'u_post',
                    'is_Active',
                    'picture',
                    'level',
                    )

    list_editable = ('u_name',
                     'u_ID',
                     'u_company',
                     'u_department1',
                     'u_department2',
                     'u_post',
                     'is_Active',
                     'picture',
                     'level',)
    search_fields = ('u_phone',)

admin.site.register(login, LoginAdmin)
