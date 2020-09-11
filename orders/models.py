from django.db import models
from shop.models import Product
from django.conf import settings
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.


class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='order')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False)
    discount = models.IntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.user}  {self.id}'

    class Meta:
        ordering=('-created',)

    def get_total_price(self):
        total= sum(i.get_cost() for i in self.item.all())
        if self.discount:
            discount_price=(self.discount/100)* total
            return int(total - discount_price)
        return total


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='item')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_item')
    quantity=models.SmallIntegerField(default=1)
    price=models.IntegerField()


    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity


class Coupon(models.Model):
    code=models.CharField(max_length=30,unique=True)
    from_date=models.DateTimeField()
    to_date=models.DateTimeField()
    discount=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active=models.BooleanField(default=False)


    def __str__(self):
        return self.code