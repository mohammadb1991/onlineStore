from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm,UserCreationForm
from .models import User
from django.contrib.auth.models import Group

# Register your models here.


class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form = UserCreationForm
    list_display = ('email','full_name','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None,{'fields':('email','full_name','password')}),
        ('personal info',{'fields':('is_active',)}),
        ('permisions',{'fields':('is_admin',)})
    )
    add_fieldsets = (
        (None,{'fields':('email','full_name','password1','password2')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User,UserAdmin)
admin.site.unregister(Group)