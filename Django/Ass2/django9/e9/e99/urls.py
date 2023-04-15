from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.user_form, name='user_form'),
    path('list/', views.user_list, name='user_list'),
]
