
from django.contrib import admin
from django.urls import path
from posts.views import registerPage,loginPage,logoutUser
urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('login/',loginPage,name='login'),
    path('register/',registerPage,name='register'),
    path('login/',logoutUser,name='logout'),
    path('',loginPage)
    
]
