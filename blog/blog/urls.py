"""blog URL Configuration

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
from django.urls import include

from editor.views import editor
from post.views import post
from tag.views import tag

urlpatterns = [
    path('admin/', admin.site.urls),
    path('editor/', include('editor.urls')),
    path('post/', include('post.urls')),
    path('tag/', include('editor.urls')),
    path('app/editor/', editor),
    path('app/post/', post),
    path('app/tag/', tag),
]
