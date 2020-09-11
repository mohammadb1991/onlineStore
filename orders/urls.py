from django.urls import path
from . import views
app_name='orders'
urlpatterns=[
    path('create/',views.create_order,name='create_order'),
    path('<int:id>/',views.detail,name='detail'),
    path('payment/<int:id>/<int:price>/',views.payment,name='payment'),
    path('verify/',views.verify,name='verify'),
    path('apply/<int:order_id>/',views.apply_coupon ,name='apply_coupon'),
    ]