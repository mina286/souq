

import re
from django.shortcuts import render,redirect
from .models import Product,Category,Image,FavoriteProduct
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .filters import ProductFilter
from django.contrib import messages
# Create your views here.
def home(request):
    context=None
    category_main = Category.objects.all().filter(CATparent__isnull=True)
   
    context ={
        'category_main':category_main

    }
    return render(request,'product/home.html',context)
#START category_page
def category_page(request,CATparent_id):
    category_sub = Category.objects.all().filter(CATparent_id=CATparent_id)
    context ={
        'category_sub':category_sub

    }
    return render(request,'product/category_page.html',context)
#END category_page

#START products
def products(request,category_id):
   
  
   
    if request.method=='GET'and 'btn_seach' in request.GET:
        products_list = Product.objects.all().filter(category_id=category_id)
        if  'free_shipping' in request.GET:
           
            free_shipping = request.GET['free_shipping']
            if free_shipping:
                products_list = Product.objects.all().filter(category_id=category_id,free_shipping=True)
       
        if  'star' in request.GET:
            star = request.GET['star']
            if star:
                products_list = Product.objects.all().filter(category_id=category_id,PRDreview=star)
        
        paginator = Paginator(products_list,20)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

     
    else:    
        products_list = Product.objects.all().filter(category_id=category_id)
        paginator = Paginator(products_list,9)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    request.session['category_id']=category_id
    context ={
        'products':products,
        

    }

    return render(request,'product/products.html',context)
#END products

#START detail_product
def detail_product(request,product_id):
    context = None
    product = Product.objects.get(id=product_id)
    if request.method == 'GET' and 'btn_addreviw' in request.GET:
        product.PRDreview=request.GET['star']
        product.save()       
        return redirect('/')
    
    if  product.PRDquantity ==  None :
        quantity = 1          
    else:
        quantity = product.PRDquantity

        
    context ={
        'product':product,
        'quantity':range(1,quantity+1)
    }

    return render(request,'product/detail_product.html',context)
#END detail_product

#add favorite_product  
def add_favorite_product(request,pro_id):
    context =None
    category_id=request.session['category_id']

    if request.method == 'GET' and 'favorite_product' in request.GET:
        if FavoriteProduct.objects.all().filter(product_id =pro_id).exists():
            messages.error(request,' هذا المنتج مضاف مسبقاالى المفضلة')
            return redirect('/detail_product/'+str(pro_id))

    if FavoriteProduct.objects.all().filter(product_id =pro_id).exists():
        messages.error(request,'هذا المنتج مضاف مسبقاالى المفضلة')
        return redirect('/products/'+str(category_id))

    
    else:
        favoriteproduct =FavoriteProduct(product_id=pro_id)
        favoriteproduct.save()
        messages.success(request,' تم اضافة المنتج الى المفضلة')       
        return redirect('/products/'+str(category_id))

#show favorite_product  
def show_favorite_product(request):
    context =None   
    favoriteproduct =FavoriteProduct.objects.all()
    context ={
        'favoriteproduct':favoriteproduct

    }         
    return render(request,'product/my_favorites.html',context)

#delete favorite_product  
def del_favorite_product(request,pro_id):
    context =None   
    #delete
    if FavoriteProduct.objects.all().filter(product_id =pro_id).exists():
        favorite_product =FavoriteProduct.objects.get(product_id=pro_id)
        favorite_product.delete()
        messages.success(request,' تم حذف المنتج من المفضلة')

    favoriteproduct =FavoriteProduct.objects.all()

    context ={
        'favoriteproduct':favoriteproduct

    }         
    return render(request,'product/my_favorites.html',context)
