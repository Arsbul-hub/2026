"""
URL configuration for webapps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, re_path
import firstapp_var_music
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', firstapp_var_music.views.index),
    re_path("music/(?P<artist_name>[^/]+)/(?P<mname>[^/]+)/?$",
            firstapp_var_music.views.search_music),
    re_path("music/(?P<mname>[^/]+)/?$",
            firstapp_var_music.views.search_music),
    re_path('^contacts', firstapp_var_music.views.contacts),
    # path('register', firstapp_var_music.views.register),
    path('login', firstapp_var_music.views.login)
]
