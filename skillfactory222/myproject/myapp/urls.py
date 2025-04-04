from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('repeat/', views.repeat_content, name='repeat'),
    path('admin-only/', views.admin_only, name='admin_only'),
]