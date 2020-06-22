from django.contrib import admin
from .models import Product, Contact

# Register your models here.

class searchAdmin(admin.ModelAdmin):
    search_fields = ('Title',)

admin.site.register(Product, searchAdmin)
admin.site.register(Contact)