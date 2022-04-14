from django.urls import path
from  .import views
urlpatterns = [
    path('signup',views.signup,name="signup"),
    path('logout_user',views.logout_user,name="logout_user"),
    path('all_accounts',views.all_accounts,name="all_accounts"),
    path('add_address',views.add_address,name="add_address"),
    path('del_address/<int:id_address>',views.del_address,name="del_address"),
    path('address_edit/<int:id_address>',views.address_edit,name="address_edit"),
    path('main_address/<int:id_address>',views.main_address,name="main_address"),
    path('address',views.address,name="address"),
    path('profile_edit/<slug:slug>',views.profile_edit,name="profile_edit"),
    path('profile/<slug:slug>',views.profile,name="profile"),

]
