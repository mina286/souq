from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignupForm,ProfileForms,UserForms,AddressForms
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import Profile,Address
# Create your views here.
def signup(request):
    context=None
    if request.method == 'POST':
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            username = signupform.cleaned_data['username']
            password1 = signupform.cleaned_data['password1']
            user =auth.authenticate(username=username,password=password1)
            if user is not None:
                auth.login(request,user)
                return redirect('/')

    else:
        signupform = SignupForm()

    context={
        'signupform':signupform

    }
    return render(request,'registration/signup.html',context)


##############logout_user#######
def logout_user(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('login')
##################my_accounts
def all_accounts(request):
        return render(request,'registration/all_accounts.html')
##################profile
@login_required(login_url='/accounts/login/')
def profile(request,slug):
    context=None
    mypofile = get_object_or_404(Profile,slug=slug)
    
    context={
        'mypofile':mypofile,
    }
    return render(request,'registration/profile.html',context)

##################profile_edit
@login_required(login_url='/accounts/login/')
def profile_edit(request,slug):
    context=None
    mypofile = get_object_or_404(Profile,slug=slug)
    userforms = UserForms(instance=request.user)
    profileforms = ProfileForms(instance=request.user.profile)
    if request.method == 'POST':
        userforms = UserForms(request.POST,instance=request.user)
        profileforms = ProfileForms(request.POST,request.FILES,instance=request.user.profile)
        if userforms and profileforms.is_valid():
            userforms.save()
            profileforms.save()
            return redirect('/')
    
    context={
        'profileforms':profileforms,
        'userforms':userforms,

    }
    return render(request,'registration/profile_edit.html',context)

##################address
@login_required(login_url='/accounts/login/')
def address(request):
    context=None
    address =Address.objects.all().filter(profile_id=request.user.profile.id)
    context={
      'address':address,

    }
    return render(request,'registration/address.html',context)

##################add_address
@login_required(login_url='/accounts/login/')
def add_address(request):
    context=None
    
    addressforms=AddressForms()
    if request.method == 'GET' and 'btn_addaddress' in request.GET:
        
        addressforms=AddressForms(request.GET)
    
        if addressforms.is_valid():
            add_address = addressforms.save(commit=False)
            add_address.profile=request.user.profile
            
            if 'rd' in request.GET and request.GET['rd'] == 'work':
                add_address.is_work  = 'True'
            else:
                add_address.is_work  = None

            if 'rd' in request.GET and request.GET['rd'] == 'home':
                add_address.is_home  = 'True'
            else:
                add_address.is_home  = None

            if 'fridaye' in request.GET:
                add_address.is_friday  = 'True'

            if 'starday' in request.GET:
                add_address.is_starday  = 'True'


            add_address.save()
            return redirect('/')

    context={
        'addressforms':addressforms
    }
    return render(request,'registration/add_address.html',context)

##################del_address
@login_required(login_url='/accounts/login/')
def del_address(request,id_address):
    address =Address.objects.get(id=id_address)
    address.delete()
  
    return redirect('address')

##################address_edit
@login_required(login_url='/accounts/login/')
def address_edit(request,id_address):
    context=None
    address =Address.objects.get(id=id_address)
    addressforms=AddressForms(instance=address)
    if request.method == 'GET' and 'btn_addaddress' in request.GET:
        
        addressforms=AddressForms(request.GET,instance=address)
    
        if addressforms.is_valid():
            add_address = addressforms.save(commit=False)
            add_address.profile=request.user.profile
            if 'rd' in request.GET and request.GET['rd'] == 'work':
                add_address.is_work  = 'True'
            else:
                add_address.is_work  = None

            if 'rd' in request.GET and request.GET['rd'] == 'home':
                add_address.is_home  = 'True'
            else:
                add_address.is_home  = None

            if 'fridaye' in request.GET:
                add_address.is_friday  = 'True'
            else:
                add_address.is_friday  = None

            if 'starday' in request.GET:
                add_address.is_starday  = 'True'
            else:
                add_address.is_starday  = None


            add_address.save()
            return redirect('/')

    context={
        'addressforms':addressforms,
        'address':address
    }
    return render(request,'registration/address_edit.html',context)


##################main_address
@login_required(login_url='/accounts/login/')
def main_address(request,id_address):
    all_address =Address.objects.all()
    address =Address.objects.get(id=id_address)

    address.is_main_address = 'True'
    for one_address in all_address:
        one_address.is_main_address = 'False'
        one_address.save()
    address.save()

    return redirect('address')
