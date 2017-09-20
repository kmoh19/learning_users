from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')



def register(request):
    
    registered=False
    
    if request.method =='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()             #.save appears to return an object....read up
            user.set_password(user.password)
            user.save()
            
            profile=profile_form.save(commit=False) # note commit=FALSE ----this is to avoid clashing with user_form instance
            profile.user=user #setting the one to one relationship between UserForm and UserProfileInfoForm appears to be a sort of coalesce step
            
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
                
            profile.save()
            
            registered=True
            
    
            
        else:
            print(user_form.errors,profile_form.errors)       
            
    else: 
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
        
        
    
    return render(request,'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})        
            
@login_required           
def user_logout (request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
      
        
        
def user_login(request):
    
    if request.method=='POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(username=username, password=password)#authenticates the user....u have to explicitly set arguments as django complains sometimes
        
        
        if user:
            if user.is_active:
                login(request,user)
                
                return HttpResponseRedirect(reverse('index'))# redirect to 'index view'
            
            else:
                return HttpResponse('Account Not Active!')
            
        else:
            print('Failed login attempt by {}'.format(username))    
            return HttpResponse('invalid login details supplied!') 
        
    else:
        return render(request,'basic_app/login.html')