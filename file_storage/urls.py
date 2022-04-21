from django.urls import path

from file_storage import views, controllers

urlpatterns = [
    path('', views.FileList.as_view(), name='file_list'),
    path('load_file', controllers.load_file, name='load_file')
]
