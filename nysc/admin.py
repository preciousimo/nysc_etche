from django.contrib import admin
from .models import Database, Inec
from import_export.admin import ExportActionMixin

# Register your models here
class DatabaseAdmin(ExportActionMixin, admin.ModelAdmin):

    list_display = ['name', 'state_code', 'ppa', 'bank_name', 'account_number']
    search_fields = ['name', 'state_code', 'ppa', 'bank_name']
    list_per_page = 20

admin.site.register(Database, DatabaseAdmin)

class InecAdmin(ExportActionMixin, admin.ModelAdmin):

    list_display = ['name', 'state_code', 'ppa', 'bank_name', 'account_number']
    search_fields = ['name', 'state_code', 'ppa', 'bank_name']
    list_per_page = 20

admin.site.register(Inec, InecAdmin)