from django.urls import path
from . import views
urlpatterns = [
    path('send_messages',views.send_messages,name="send_messages"),
]