from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    slug = models.SlugField(blank=True,null=True)
    image = models.ImageField(upload_to='profile_photo/%Y/%m/%d/',verbose_name='الصوره الرئيسية للعميل',blank=True,null=True)
    join_date = models.DateTimeField(default=datetime.now)
    phone_number = models.IntegerField(null=True,blank=True)
 
    def save(self,*args,**kwargs): 
        if not self.slug:
            self.slug=slugify(self.user.username)
        super(Profile, self).save(*args,**kwargs)

    def create_profile(sender,**kwargs):
        if kwargs['created']:
            Profile.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile,sender=User)

    def __str__(self) :
        return self.user.username
        
class  Address(models.Model):
 
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    country = models.CharField(max_length=150,verbose_name="البلد")
    phone_number = models.IntegerField(verbose_name="رقم الموبيل")
    Street_name = models.CharField(max_length=200,blank=True,null=True,verbose_name="اسم الشاع")
    Building_name_or_number =models.CharField(blank=True,null=True,max_length=150,verbose_name="اسم/رقم المبنى، رقم الطابق، رقم الشقة، أو رقم الفيلا")
    Region = models.CharField(max_length=150,verbose_name="المنطقة/المدينة")
    district= models.CharField(max_length=150,blank=True,null=True,verbose_name="الحى")
    Governorate = models.CharField(max_length=150,verbose_name="المحافظة")
    nearest_mark= models.CharField(max_length=200,blank=True,null=True,verbose_name="أقرب علامة مميزة")
    is_home=models.BooleanField(blank=True,null=True,verbose_name="المنزل")
    is_work=models.BooleanField(blank=True,null=True,verbose_name="العمل")
    is_friday=models.BooleanField(blank=True,null=True,verbose_name="الجمعة")
    is_starday=models.BooleanField(blank=True,null=True,verbose_name="السبت")
    is_main_address=models.BooleanField(blank=True,null=True,verbose_name="عنوان ئيسي")

    def __str__(self) :
        return self.profile.user.first_name+' '+self.profile.user.last_name+' '+'id='+str(self.profile.user.id)

