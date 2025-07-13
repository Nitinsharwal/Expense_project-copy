from django.db import models

# Create your models here.
class current_ammount(models.Model):
    current_balance = models.FloatField(default=0)
class Tracker(models.Model):
    current_balance = models.ForeignKey(current_ammount, on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=100,choices=(("Credit","Credit"),("Debit","Debit")))
    ammount = models.FloatField(default=0)
    description = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now_add=True)