"""police URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from ukPolice.views import main, signup, home

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^signup$', signup, name='signup'),
    url(r'^login$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^logout$', logout, {'template_name': 'main.html', }, name="logout"),
    url(r'^home$', home, name='home'),
    url(r'^admin/', admin.site.urls),
]

#urlpatterns = [
    #url(r'^ukPolice/', include('ukPolice.urls', namespace='ukPolice')),
    #url(r'^accounts/login/$', login, name='login'),
    #url(r'^accounts/logout/$', logout, name='logout'),
    #url(r'^profile/(\w+)/$', dashboard), # Expressio regular-->Qualsevol lletra que conformi una paraula sense linies
    #url(r'^$', views.index, name='login'),
    #url(r'^$', login, {'template_name':'index.html'}, name='login'),
    #url(r'^admin/', admin.site.urls),
#]
