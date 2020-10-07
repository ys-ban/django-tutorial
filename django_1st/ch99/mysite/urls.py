"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static  # photo 앱에 필요
from django.conf import settings    # photo 앱에 필요

from mysite.views import HomeView

from mysite.views import UserCreateView, UserCreationDoneTV       # login view

#from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    path('admin/', admin.site.urls),
    # home view
    path('', HomeView.as_view(), name='home'),
    # 인증 관련 URL
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreationDoneTV.as_view(), name='register_done'),
    # 추가 app
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),
    # class based view
    #path('bookmark/', BookmarkLV.as_view(), name = 'index'),
    #path('bookmark/<int:pk>/', BookmarkDV.as_view(), name = 'detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #photo 앱에 필요
