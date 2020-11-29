from django.contrib import admin
from api.models import CompanyScrip

# Register your models here.

class CompanyScripAdmin(admin.ModelAdmin):

    list_display = ("company_name", "scrip_codes")

admin.site.register(CompanyScrip, CompanyScripAdmin)