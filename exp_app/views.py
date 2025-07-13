from django.shortcuts import render,redirect
from .models import Tracker,current_ammount
# Create your views here.

def home(request):
    if request.method == "POST":
        description = request.POST.get('description')
        ammount = request.POST.get('ammount')
        current_balance, _ = current_ammount.objects.get_or_create(id = 1)
        expense_type = "Credit"
        if float(ammount) < 0:
            expense_type = "Debit"
        tracking = Tracker.objects.create(
        ammount=ammount,expense_type=expense_type,
        current_balance=current_balance,
        description=description)
        current_balance.current_balance += float(tracking.ammount)
        current_balance.save()
        return redirect('/')
    return render(request, 'base.html')