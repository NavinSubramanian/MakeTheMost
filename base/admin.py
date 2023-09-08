from django.contrib import admin

# Register your models here.

from .models import *

class ContentAdmin(admin.ModelAdmin):
    list_display=('name','img','number','link')
    search_fields=Items.SearchableFields

admin.site.register(Items,ContentAdmin)
admin.site.register(Waste)