from django.shortcuts import render,get_object_or_404,redirect
from cart.cart import Cart
from .models import Order,OrderItem,Coupon
from django.contrib.auth.decorators import login_required
from suds.client import Client
from django.http import HttpResponse
from django.contrib import messages
from .forms import CouponForm
from django.utils import timezone
from django.views.decorators.http import require_POST
# Create your views here.


@login_required
def detail(request,id):
    order=get_object_or_404(Order,id=id)
    form=CouponForm()
    return render(request,'orders/order.html',{'order':order,'form':form})


@login_required
def create_order(request):
    cart = Cart(request)
    order=Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order,product=item['product'],quantity=item['quantity'],price=item['price'])
    cart.clear()
    return redirect('orders:detail',order.id)

MERCHANT = 'a2702920-041b-11e7-ae98-000c295eb8fc'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')

description = "پرداخت گلکسی اسپورت"  # Required
mobile = '09179070370'  # Optional
CallbackURL = 'http://localhost:8000/orders/verify/'

@login_required
def payment(request,id,price):
    global amount, o_id
    amount =price
    o_id=id
    result = client.service.PaymentRequest(MERCHANT, amount, description, request.user.email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


@login_required
def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            order=Order.objects.get(id=o_id)
            order.paid=True
            order.save()
            messages.success(request,'you paid successfully','success')
            return redirect('shop:home')
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')



def apply_coupon(request,order_id):
    now=timezone.now()
    form=CouponForm(request.POST)
    if form.is_valid():
        code=form.cleaned_data['code']
        try:
            coupon=Coupon.objects.get(code__iexact=code,from_date__lte=now,to_date__gte=now,active=True)
        except Coupon.DoesNotExist:
            messages.error(request,'this coupen Does not exist','danger')
            return redirect('orders:detail' , order_id)
        order=Order.objects.get(id=order_id)
        order.discount=coupon.discount
        order.save()
    return redirect('orders:detail',order_id)
