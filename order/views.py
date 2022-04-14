from django.shortcuts import render,redirect
from .models import Order,OrderDetails 
from product.models import Product
from  django.contrib import messages
from accounts.models import Address
# Create your views here.
#add_to_cart
def add_to_cart(request,pro_id):
    quntity=1
    if request.method == 'GET' or 'btn_addcart' in request.GET :
        print("ttttttttt hghgfhfh")
        if 'select_quntity' in request.GET:
            quntity =request.GET['select_quntity']
        # if user call order and not fnish it
        if Order.objects.all().filter(user=request.user,is_finish=False).exists():
            
                order =Order.objects.get(user=request.user,is_finish=False)
                product = Product.objects.get(id=pro_id)

                # if product already exists in cart but need to change quantity
                if OrderDetails.objects.all().filter(product=product,order=order).exists():
                   
                    #check discount is found or not
                    if  product.PRDdiscountprice !=  None and product.PRDdiscountprice >= 1:
                        price = product.PRDdiscountprice            
                    else:
                        price = product.PRDprice

                    orderdetails = OrderDetails.objects.get(order=order,product_id=pro_id)
                    orderdetails.ODquantity =quntity
                    orderdetails.ODprice =price

                    if 'quantity_from_detailproduct' in request.GET:
                        orderdetails.save()

                    if 'quantity_from_cart' in request.GET:
                        if int(quntity) > product.PRDquantity:
                                messages.error(request,' غير متاح كل هذة الكمية عند البائع')
                                return redirect('show_cart')
                        orderdetails.save()
                        messages.success(request,'تم تغير كمية المنتج بنجاح')
                        return redirect('show_cart')

                     # from page favorite product
                    if 'from_fav_product' in request.GET:
                        messages.error(request,' هذا المنتج مضاف مسبقا فى عربة التسوق')
                        return redirect('show_favorite_product')


                    messages.success(request,'تم الاضافه الى عربة التسوق')
                    return redirect('/detail_product/'+str(pro_id))
                else:# if product is new                
                    #check discount is found or not
                    if  product.PRDdiscountprice !=  None and product.PRDdiscountprice >= 1:
                        price = product.PRDdiscountprice            
                    else:
                        price = product.PRDprice
                    
                    orderdetails =OrderDetails.objects.create(order=order,product=product,ODquantity=quntity,ODprice=price)
                    orderdetails.save()  
                    # from page favorite product
                    if 'from_fav_product' in request.GET:
                        messages.success(request,'تم الاضافه الى عربة التسوق')
                        return redirect('show_favorite_product')    
                                                   
                    messages.success(request,'تم الاضافه الى عربة التسوق')
                    return redirect('/detail_product/'+str(pro_id))

        else:# if user call order and  fnish it and call new order id
            order =Order.objects.create(user=request.user)
            order.save()
            product = Product.objects.get(id=pro_id)
             #check discount is found or not
            if  product.PRDdiscountprice !=  None and product.PRDdiscountprice >= 1:
                price = product.PRDdiscountprice            
            else:
                price = product.PRDprice

            orderdetails =OrderDetails.objects.create(order=order,product=product,ODquantity=quntity,ODprice=price)
            orderdetails.save()   
            messages.success(request,'تم الاضافه الى عربة التسوق')
            return redirect('/detail_product/'+str(pro_id))

#show cart
def show_cart(request):
    context=None
    if Order.objects.all().filter(user=request.user,is_finish=False).exists():
        order =Order.objects.get(user=request.user,is_finish=False)
        orderdetails = OrderDetails.objects.all().filter(order=order)

        #sum of quantity all peoduct in oerderdetails
        sum_product_of_orderdetials = 0
        sum_price=0
        orderdetails_tosum = OrderDetails.objects.all().filter(order=order,is_showin_cart=True)
        for qnt_pro in orderdetails_tosum:
            sum_product_of_orderdetials+= qnt_pro.ODquantity
            #sum of price  all peoduct in oerderdetails
            sum_price +=qnt_pro.ODquantity*qnt_pro.ODprice
        order.total_order=sum_price
        order.save()  

        quantity=10

        request.session['sum_product_of_orderdetials']=sum_product_of_orderdetials
        context ={
            'order':order,
            'orderdetails':orderdetails,
            'quantity':range(1,quantity+1),    
            'sum_price':sum_price,
        
        }
    if Order.objects.filter(user=request.user).last().is_finish == True:
        request.session['sum_product_of_orderdetials']='yes_true'

    return render(request,'order/cart.html',context)
   
#delete product from cart
def delete_product_cart(request,pro_id):
    order =Order.objects.get(user=request.user,is_finish=False)
    orderdetails = OrderDetails.objects.get(order=order,product=pro_id)
    messages.success(request,f'{orderdetails.product.PRDname},تم حذفه من عربة التسوق')
    orderdetails.delete()
    return redirect('show_cart')

#active or not product in  cart
def active_product_cart(request,pro_id):
    if request.method == 'GET' :
        order =Order.objects.get(user=request.user,is_finish=False)
        orderdetails = OrderDetails.objects.get(order=order,product=pro_id)

        if 'status_active' in request.GET:            
            is_showin_cart=True
            orderdetails.is_showin_cart=is_showin_cart
            orderdetails.save()
            messages.success(request,',تم  احتساب المنتج فى العربة')       

          
        else:            
                is_showin_cart=False
                orderdetails.is_showin_cart=is_showin_cart
                orderdetails.save()
                messages.success(request,', تم عدم احتساب المنتج والسعر فى العربة')  

    return redirect('show_cart')

#order_history   buy_addressselecte
def order_history(request):
    context=None
    order_list =Order.objects.all().filter(user=request.user,is_finish=True)
    #sum of quantity all peoduct in oerderdetails   
    context = {
        'order_list':order_list,
       
        

    }
    return render(request,'order/order_history.html',context)


#  buy_addressselecte
def buy_addressselecte(request):
    context=None
    address =Address.objects.all().filter(profile=request.user.profile)
    order =Order.objects.get(user=request.user,is_finish=False)

    context ={
        'address':address,
        'order':order,
    }
    return render(request,'order/buy_addressselecte.html',context)
