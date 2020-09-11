from django.contrib import admin
from .models import Order,OrderItem,Coupon
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','created','updated','paid')
    list_filter = ('paid',)
    inlines = (OrderItemInline,)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code','from_date','to_date','discount','active')
    list_filter =('active','from_date','to_date')
    search_fields = ('code',)