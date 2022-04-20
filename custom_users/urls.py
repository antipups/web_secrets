from django.urls import path

from custom_users import controllers, views

urlpatterns = [
    path('login', controllers.auth, name='auth'),
    path('singup', views.CreateUser.as_view(), name='signup')
]
