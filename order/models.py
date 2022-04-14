from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_created = models.DateTimeField(default=datetime.now)
    is_finish = models.BooleanField(default=False)
    total_order=models.DecimalField(max_digits=9,decimal_places=2,verbose_name=' مجمل الاورد',default=0)

    def __str__(self):
        return str(self.id)+'-----'+self.user.username+' '+str(self.is_finish)

class OrderDetails(models.Model):
   
    order = models.ForeignKey('Order',on_delete=models.CASCADE,verbose_name=' الاورد')
    product = models.ForeignKey('product.Product',on_delete=models.CASCADE,verbose_name=' المنتج')
    ODquantity = models.IntegerField(verbose_name=' الكمية')
    ODprice = models.DecimalField(max_digits=9,decimal_places=2,verbose_name=' السعر')
    is_showin_cart =models.BooleanField(default=True,verbose_name='الظهور فى العربة')
    def total_price(self):
        return self.price * self.quantity
    def __str__(self):
        return 'oredertails id='+ str(self.id)+'-----'+self.product.PRDname+'product id= '+str(self.product.id)+'order id='+str(self.order.id)
