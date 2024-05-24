"""
URL configuration for Core project.

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
from django.urls import include, path
from django.conf import settings
from Core.views import SystemView

urlpatterns = [
    # Dashboard urls applied to admin
    #path('admin/', admin.site.urls),  
    path('admin/', include('dashboards.urls')),
    path('admin/', include('auth.urls')),
]

handler404 = SystemView.as_view(template_name = 'pages/' + settings.KT_THEME + '/system/not-found.html', status=404)
handler500 = SystemView.as_view(template_name = 'pages/' + settings.KT_THEME + '/system/error.html', status=500)
