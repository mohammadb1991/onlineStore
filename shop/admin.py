from django.contrib import admin
from .models import Category,Product

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}



@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ('name','price','availble')
    list_filter = ('availble','created')
    list_editable = ('price','availble')
    prepopulated_fields = {'slug':('name',)}
    raw_id_fields = ('category',)
# Register your models here.
