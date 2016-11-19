"""projectile URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from mainapp.forms import LoginForm
from django.contrib.auth import views
import notifications.urls
from django.contrib.auth.decorators import user_passes_test


login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('mainapp.urls')),
    url(r'^login/$', login_forbidden(views.login), {'template_name': 'user_login.html', 'authentication_form': LoginForm}, name='login',),
    url(r'^logout/$', views.logout, {'next_page': '/login'}, name='logout'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),

]
