from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('Register/',views.register_user,name='Register'),
    path('Success_page/',views.Success_page,name='Success'),
]