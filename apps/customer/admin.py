from django.contrib import admin

# Register your models here.
from .models import Customer


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
