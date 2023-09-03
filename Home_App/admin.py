from django.contrib import admin
from Home_App.models import Book_Table, Employees, Items

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('item_title', 'item_decription', 'item_price', 'item_quantity', 'item_image')

admin.site.register(Book_Table)
admin.site.register(Employees)
admin.site.register(Items)