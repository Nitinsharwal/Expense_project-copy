from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('del-history/<id>/',views.del_history,name='del_history'),
]