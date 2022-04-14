from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):

    PRDname = models.CharField(max_length=100,verbose_name='اسم المنتج')
    category=models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name=' التصنيف',blank=True,null=True)
    brand=models.ForeignKey('Brand',on_delete=models.CASCADE,verbose_name=' البراند',blank=True,null=True)
    PRDdesc=models.TextField(verbose_name='وصف المنتج')
    PRDprice = models.DecimalField(max_digits=9,decimal_places=2,verbose_name='السعر ')
    PRDdiscountprice = models.DecimalField(max_digits=9,decimal_places=2,verbose_name='الخصم ',null=True,blank=True)
    PRDcost = models.DecimalField(max_digits=9,decimal_places=2,verbose_name=' التكلفه')
    PRDcreated =models.DateTimeField(verbose_name=' وقت اضافة المنتج')
    PRDimage = models.ImageField(upload_to='product_photo/%Y/%m/%d/',verbose_name='الصوره الرئيسية للمنتج')
    PRDslug = models.SlugField(null=True,blank=True,verbose_name="slug",allow_unicode=True)
    PRDisnew = models.BooleanField(default=False,verbose_name='منتج مضاف حديثا')
    PRDisbeatsaller = models.BooleanField(default=False,verbose_name='  منتج الاكثر مبيعا')
    PRDreview = models.CharField(max_length=6,blank=True,null=True,verbose_name='معدل التقيم')
    PRDquantity = models.IntegerField(verbose_name='الكميه فى المخزن ',blank=True,null=True)
    PRDisdiscount = models.BooleanField(default=False,verbose_name='خصومات  ')
    free_shipping = models.BooleanField(default=False,verbose_name='شحن مجانى  ')
    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"
    
    def save(self,*args,**kwargs):
        if not self.PRDslug:
            self.PRDslug = slugify(self.PRDname)
            super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return self.PRDname

class Image(models.Model):
   PRDIprodcut=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='المنتج')
   PRDIimage = models.ImageField(upload_to='product_photo/%Y/%m/%d/',verbose_name='صوره المنتج')
   class Meta:
        verbose_name="Image"
        verbose_name_plural="Imagies"
   def __str__(self):
        return str(self.PRDIprodcut)

class Category(models.Model):
    CATname= models.CharField(max_length=100,verbose_name=' اسم التصنيف')
    CATparent=models.ForeignKey('self',limit_choices_to={'CATparent__isnull':True},on_delete=models.CASCADE,null=True,blank=True,verbose_name=' التصنيف الرئيسي')
    CATdesc=models.TextField(verbose_name='وصف التصنيف')
    CATimage = models.ImageField(upload_to='category/%Y/%m/%d/',verbose_name='صوره التصنيف')
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
    def __str__(self):
        return self.CATname

class Product_alternative(models.Model):
    PALNproduct= models.ForeignKey(Product,related_name='main_product',on_delete=models.CASCADE,verbose_name=' اسم المنتج')
    PALNalternatives= models.ManyToManyField(Product,related_name='alternative_product',verbose_name=' اسم البدائل')
    class Meta:
        verbose_name="Product_alternative"
        verbose_name_plural="Product_alternativeies"
    def __str__(self):
        return str(self.PALNproduct)

class Product_accessor(models.Model):
    PACCproduct= models.ForeignKey(Product,related_name='main_accessory',on_delete=models.CASCADE,verbose_name=' اسم المنتج')
    PACCalternatives= models.ManyToManyField(Product,related_name='accessory_product',verbose_name=' اسم البدائل')
    
    class Meta:
        verbose_name="Product_accessor"
        verbose_name_plural="Product_accessories"
    def __str__(self):
        return str(self.PACCproduct)

class Brand(models.Model):
    BRNname= models.CharField(max_length=100,verbose_name=' اسم البراند')
    BRNdesc= models.CharField(max_length=100,verbose_name='  وصف البراند',null=True,blank=True)

    class Meta:
        verbose_name="Brand"
        verbose_name_plural="Brands"
    def __str__(self):
        return self.BRNname

class Variant(models.Model):
    VARname= models.CharField(max_length=100,verbose_name=' اسم البديل')
    VARdesc= models.CharField(max_length=100,verbose_name='  وصف البديل',null=True,blank=True)

    class Meta:
        verbose_name="Variant"
        verbose_name_plural="Variants"
    def __str__(self):
        return self.VARname


class FavoriteProduct(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='المنتج')
    def __str__(self):
        return self.product.PRDname
    