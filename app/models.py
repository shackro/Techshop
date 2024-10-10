from django.contrib.auth.models import User
from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('IP16','iphone16 '),
    ('IP15','iphone15 '),
    ('IP14','iphone14 '),
    ('IP14','iphone13 '),
    ('IP12','iphone12 '),
    ('IP11','iphone11 '),
    ('IP11','iphone11 '),
    ('IP10','iphone10 '),
    ('IP9','iphone9 '),
    ('IP8','iphone8 '),
    ('IPR15','iphone_refubrish15'),
    ('IPR14','iphone_refubrish14'),
    ('IPR13','iphone_refubrish13'),
    ('IPR12','iphone_refubrish12'),
    ('IPR11','iphone_refubrish11'),
    ('IPR10','iphone_refubrish10'),
    ('IPR9','iphone_refubrish9'),
    ('IPR8','iphone_refubrish8'),
)

class Product(models.Model):
    title =models.CharField(max_length=100,null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    discount_price=models.FloatField(null=True)
    description =models.TextField(null=True)
    composition =models.TextField(default='',null=True)
    category =models.CharField(max_length=6,choices=CATEGORY_CHOICES,default='General')
    product_image =models.ImageField(upload_to='products/',null=True)
    def __str__(self):
        return self.title



class Customer(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile =models.IntegerField(default=0)
    zipcode = models.IntegerField()
    def __str__(self):
        return self.name

class Cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price


Status_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Accepted'),
    ('ON The Way','On The Way'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),

)
class Payment(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    amount =models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=40, choices=Status_CHOICES ,default='Pending')
    payment =models.ForeignKey(Payment,on_delete=models.CASCADE,default='')
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price
