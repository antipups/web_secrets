from django.urls import path

from file_storage import views

urlpatterns = [
    path('', views.FileList.as_view, name='file_list')
]
