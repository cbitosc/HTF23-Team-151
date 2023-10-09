from django.shortcuts import render,redirect

# Create your views here.
from events.models import Profile,clubevents,emailid
from django.contrib import messages
from django.http import HttpResponse
from .forms import paperform


from events.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,"homepage.html")

'''def login(request) :
    if request.method=='POST' :
        global username
        username=request.POST['username']
        password=request.POST['password']
        teach_list=club.objects.all()
        for i in teach_list :
            if i.email==username and i.password==password:
                return redirect("/teacherview")
        else :
            messages.info(request,'Invalid username or password')
            return redirect('/login')
    else  :
        return render(request,'login.html')'''
    
def login_attempt(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('username')
        password = request.POST.get('password')


        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/accounts/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/accounts/login')

        user = authenticate(username = username , password = password)
        if user is None:
            print(username,password)
            messages.success(request, 'Wrong password.')
            return redirect('/accounts/login')
        
        login(request , user)
        return redirect('/teacherview/')

    return render(request , 'login.html')



def teachview(request) :
    research=clubevents.objects.all()
    for i in research:
        if i.cname==username:
            desc=i.cdesc
    print(research,username)
    return render(request,'teachview.html',{'research':research,'username':username,'desc':desc})

def delete(request, id):
        record_to_delete =clubevents.objects.get(id=id)
        record_to_delete.delete()
        return redirect('/teacherview/')

def edit(request, id):
    research=clubevents.objects.get(id=id)
    return render(request, 'edit.html', {'research':research})

def update(request,id) :
    research=clubevents.objects.get(id=id)
    form=paperform(request.POST,instance=research)
    if (form.is_valid()):
        form.save()
        return redirect('/teacherview/')
    return render(request,'edit.html',{'research':research,'username':username})

def add(request):
    research=clubevents.objects.all()
    for i in research:
        if i.cname==username:
            res=i
            break
    res.pk=None
    res.save()
    return render(request, 'add.html', {'res':res})

def addnew(request,id):
    research=clubevents.objects.get(id=id)
    form=paperform(request.POST,instance=research)
    if (form.is_valid()):
        form.save()
        return redirect('/teacherview/')
    return render(request,'add.html',{'research':research})


def viewers_page(request):
    research = clubevents.objects.all()

    return render(request, 'viewers.html', {'research': research})

'''def viewers_info(request,name) :
    research=clubevents.objects.filter(ename=name)
    return render(request, 'view2.html', {'research':research})'''

#*****************************************************************************************************************************

def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        emails=emailid.objects.all()
        count=0
        for i in emails:
            if i.temail==email:
                count+=1
        if count==0:
            messages.success(request, 'Email does not belong to a club')
            return redirect('/register')


        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)


    return render(request , 'register.html')

def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/accounts/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')


def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list)
