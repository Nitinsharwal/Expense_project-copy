from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login_view/',views.login_view,name='login_view'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('register_view/',views.register_view,name='register_view'),
    path('profile/',views.profile,name='profile'),
    path('del-history/<id>/',views.del_history,name='del_history'),
]