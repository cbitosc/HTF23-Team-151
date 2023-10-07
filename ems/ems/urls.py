"""
URL configuration for ems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from events import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    #path('login/',views.login),
    path('teacherview/',views.teachview),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('add/',views.add,name='add'),
    path('addnew/<int:id>',views.addnew,name='addnew'),
    path('viewers/',views.viewers_page,name='viewers_page'),
    #path('view2/<str:name>',views.viewers_info,name='view2'),
    #*******************************************
    #path('' ,  views.home  , name="home"),
    path('register/' , views.register_attempt , name="register_attempt"),
    path('accounts/login/', views.login_attempt , name="login_attempt"),
    path('token' ,views.token_send , name="token_send"),
    path('success' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error' ,views.error_page , name="error"),

]
