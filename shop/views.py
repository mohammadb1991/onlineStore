from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.forms import CartAddForm

# Create your views here.

def home(request,slug=None):
    products=Product.objects.filter(availble=True)
    categorys =Category.objects.filter(is_sub=False)
    if slug:
        category=get_object_or_404(Category,slug=slug)
        products=products.filter(category=category)
    return render(request,'shop/home.html',{'products':products,'categorys':categorys})


def detail_product(request,slug):
    products=get_object_or_404(Product,slug=slug)
    form=CartAddForm()
    return render(request,'shop/detail_product.html',{'product':products,'form':form})



