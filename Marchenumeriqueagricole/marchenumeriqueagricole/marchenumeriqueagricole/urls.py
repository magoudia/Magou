"""
URL configuration for marchenumeriqueagricole project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from AgriTech import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('product/',views.product,name='product'),
    path('blog/',views.blog,name='blog'),
    path('detail/',views.blog,name='detail'),
    path('feature/',views.feature,name='feature'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.contact,name='service'),
    path('', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('legumes/', views.legumes, name='legumes'),
    path('produits/', views.produits, name='produits'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)