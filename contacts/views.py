from django.conf import settings
from django.shortcuts import render
from  .models import  Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def send_messages(request):
    myinfo =Info.objects.first()
    error = None
    if request.method=='POST':
        email = 'minalotfy05@gmail.com'
        subject = request.POST['subject']
        message = request.POST['message']

        if subject and message:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
            )
            

        else:
            error=True
               
       # print(email+subject+message)
    context={
        'myinfo':myinfo,
        'error':error
    }
    return render(request,'contacts/contact.html',context)