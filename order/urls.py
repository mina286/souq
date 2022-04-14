from django.urls import path
from . import views
urlpatterns = [
    path('add_to_cart/<int:pro_id>',views.add_to_cart,name="add_to_cart"),
    path('show_cart',views.show_cart,name="show_cart"),
    path('delete_product_cart/<int:pro_id>',views.delete_product_cart,name="delete_product_cart"),
    path('active_product_cart/<int:pro_id>',views.active_product_cart,name="active_product_cart"),
    path('order_history',views.order_history,name="order_history"),
    path('buy_addressselecte',views.buy_addressselecte,name="buy_addressselecte"),

]