from django.shortcuts import render,redirect
from .models import Tracker,current_ammount
from django.db.models import  Sum
from django.utils.timezone import now
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="login_view")
def home(request):
    if request.method == "POST":
        description = request.POST.get('description')
        ammount = request.POST.get('ammount')
        current_balance, _ = current_ammount.objects.get_or_create(id = 1)
        expense_type = "Credit"
        if float(ammount) < 0:
            expense_type = "Debit"
        if float(ammount) == 0:
            messages.error(request,"Amount Can't be zero..!")
            return redirect('/')
        tracking = Tracker.objects.create(
        ammount=ammount,expense_type=expense_type,
        current_balance=current_balance,
        description=description)
        current_balance.current_balance += float(tracking.ammount)
        current_balance.save()
        messages.success(request,'Your Expense has been Added..!')
        return redirect('/')
    
    income = 0
    expense = 0
    for tracking in Tracker.objects.all():
        if tracking.expense_type == "Credit":
            income+=tracking.ammount
        else:
            expense+=tracking.ammount
    current_balance, _ = current_ammount.objects.get_or_create(id = 1)
    context =  {'transactions': Tracker.objects.all(),'current_balance':current_balance,'income':income,'expense':expense,'now': now()}
    
    return render(request, 'base.html',context)

def del_history(request,id):
    tracking = Tracker.objects.filter(id=id)
    tracking.delete()
    return redirect('/')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if not user.exists():
            messages.error(request, "User not found...!")
            return redirect('/login_view/') 
        
        user = authenticate(username=username, password=password)
        if not user:
            messages.error(request, "Incorrect Password...!")
            return redirect('/login_view/') 
        
        login(request, user)
        return redirect('/')
    
    return render(request, 'login_view.html')  
def logout_view(request):
    logout(request)
    return redirect('/login_view/')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')

        if len(password) < 8:
            messages.warning(request, "Your password is too short..")
            return redirect('/register_view/')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "User already exists...!")
            return redirect('/login_view/')  

        user = User.objects.create(
            username=username,
            first_name=firstname,
            last_name=lastname,
            email=email
        )
        user.set_password(password)
        user.save()

        current_balance, _ = current_ammount.objects.get_or_create(id=1)
        current_balance.current_balance = 0
        current_balance.save()

        Tracker.objects.all().delete()

        messages.success(request, 'Account Created..!')
        return redirect('/login_view/')  

    return render(request, 'register_view.html')

def profile(request):
    return render(request, "profile.html")
