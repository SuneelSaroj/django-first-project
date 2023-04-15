from django.contrib import admin
from .models import Emp


# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'department',
                    'emp_id', 'is_working', 'address',)
    list_editable = ('name', 'mobile', 'is_working',)
    search_fields = ('name',)
    list_display_links = None

    def __str__(self):
        return self.name


admin.site.register(Emp, EmpAdmin)
