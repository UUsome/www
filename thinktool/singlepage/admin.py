from django.contrib import admin
from .models import contact
# Register your models here.
@admin.register(contact)
class contact(admin.ModelAdmin):
    list_display = ('title', 'contact', 'content', 'add_time',)



