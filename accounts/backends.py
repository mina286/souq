import email
from operator import truth
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib import messages
class  EmailOrUsername(ModelBackend):
    def authenticate(self,request,username=None,password=None,**kwargs):
        '''check username or email  is found'''
        try:
            user = User.objects.get(
                 #login usernam only  Q(username__iexact=username)
                  #login emal only  Q(email__iexact=username) 
                Q(username__iexact=username) |
                Q(email__iexact=username) 
            )
        except User.DoesNotExist:
            return messages.error(request,'Your username or Email didnt match. Please try again.')

        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by('id').first()
        else:
            '''check is password is coorect and is can authenticated for him'''
            if user.check_password(password) and self.user_can_authenticate(user) :
                return user
    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
