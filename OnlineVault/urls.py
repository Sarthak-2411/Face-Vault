"""OnlineVault URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from authentication import views as authentication_views
from face_recog import views as face_recog_views
from home_page import views as home_page_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',authentication_views.login_signup,name='login_signup'),
    path('logout/',authentication_views.user_logout,name='logout'),
    path('auth/',authentication_views.authentication,name='authenticate'),

    # path('webcam/<int:status>',face_recog_views.webcam,name='webcam'),
    # path('capture_face/',face_recog_views.capture_face,name='capture_face'),
    
    path('home/',home_page_views.home,name='home'),
    path('404/',authentication_views.page_not_found,name='page_not_found'),
    path('capture_store/<int:status>',face_recog_views.capture_and_store,name='captureandstore'), # This is for testing 

    path('upload/',home_page_views.upload_file,name='upload_file'),
    path('delete/<str:name>',home_page_views.delete_file,name='delete_file'),
    path('edit/<str:old_name>/<str:new_name>',home_page_views.edit_file,name='edit_file'),

    path('download/<str:file>',home_page_views.download,name='download'),
    path('open/<str:file>',home_page_views.open_file,name='open_file'),    

]
