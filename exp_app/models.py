from django.db import models

# Create your models here.
class current_ammount(models.Model):
    current_balance = models.FloatField(default=0)
    def __str__(self):
        return str(self.current_balance)
    
class Tracker(models.Model):
    current_balance = models.ForeignKey(current_ammount, on_delete=models.CASCADE,editable=False)
    expense_type = models.CharField(max_length=100,choices=(("Credit","Credit"),("Debit","Debit")))
    ammount = models.FloatField(default=0,editable=False)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.current_balance,self.expense_type,self.ammount,self.description
    