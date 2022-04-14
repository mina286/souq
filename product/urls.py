from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('category_page/<int:CATparent_id>',views.category_page,name="category_page"),
    path('products/<int:category_id>',views.products,name="products"),
    path('detail_product/<int:product_id>',views.detail_product,name="detail_product"),
    path('add_favorite_product/<int:pro_id>',views.add_favorite_product,name="add_favorite_product"),
    path('del_favorite_product/<int:pro_id>',views.del_favorite_product,name="del_favorite_product"),
    path('show_favorite_product',views.show_favorite_product,name="show_favorite_product"),

]
