"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import mydiary.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mydiary.views.home,name="home"),
    path('new/', mydiary.views.new,name="new"),
    path('detail/<int:index>',mydiary.views.detail, name="detail"),
    path('edit/<int:index>',mydiary.views.edit, name="edit"),
    path('detail/<int:pk>/delete',mydiary.views.delete, name="delete"),
    path('detail/<int:index>/comment/<int:comment_pk>/delete/',mydiary.views.delete_comment, name="delete_comment"),
    path('tagadd/<int:pk>', mydiary.views.tag_add, name="tag_add"),
    path('tag',mydiary.views.tag_home, name="tag_home"),
    path('hashtag/<int:pk>', mydiary.views.tag_detail,name="tag_detail"),
    path('detail/<int:pk>/tag/<int:tag_pk>/delete', mydiary.views.tag_delete,name="tag_delete"),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)