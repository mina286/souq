from django.db import models

# Create your models here.
class Info(models.Model):
    infplace=models.CharField(max_length=100,verbose_name='المكان')
    infphone_number=models.CharField(max_length=20,verbose_name='الموبيل')
    infemail=models.EmailField(max_length=200)
    def __str__(self) :
        return self.infemail