from django.contrib import admin
from .models import product , customer


# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'buy',"number"]
    search_fields = ['name']
    
    
    
class customerAdmin(admin.ModelAdmin):
    list_display = ['author', 'phone', 'city']
    search_fields = ['author','phone','city']
    filter_horizontal = ['basket']



admin .site.register(product,productAdmin)
admin .site.register(customer,customerAdmin)

