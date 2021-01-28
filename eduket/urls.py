"""eduket URL Configuration

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
from django.urls import path, include
from student import views as stu
from teacher import views as tech
from main import views as m
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',m.login),
    path('home/',m.home),
    path('about/',m.about),
    path('login/',m.login),
    path('signin/',m.signin),
    path('stu_detail/',stu.stu_detail),
    path('logout/',m.logout),
    path('middle/',m.middle),
    path('teacher_detail/',tech.teacher_detail),
    path('upload/',tech.upload_doc),
    path('profile/',m.profile),
    path('delete/',m.delete),
    path('account/',m.account),
    path('security/', include('django_mfa.urls')),
    path('search/',m.search),
    path('category/',m.cate_show),
    path('pdf/',m.pdf_view),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
