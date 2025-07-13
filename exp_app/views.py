from django.shortcuts import render,redirect
from .models import Tracker,current_ammount
from django.db.models import  Sum
from django.utils.timezone import now
from django.contrib import messages

def home(request):
    if request.method == "POST":
        description = request.POST.get('description')
        ammount = request.POST.get('ammount')
        current_balance, _ = current_ammount.objects.get_or_create(id = 1)
        expense_type = "Credit"
        if float(ammount) < 0:
            expense_type = "Debit"
        if float(ammount) == 0:
            messages.warning(request,"Amount Can't be zero..!")
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