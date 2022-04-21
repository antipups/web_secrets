from django.conf.urls.static import static
from django.urls import path

from file_storage import views, controllers
from web_secrets import settings

urlpatterns = [
    path('', views.FileList.as_view(), name='file_list'),
    path('load_file', controllers.load_file, name='load_file'),
    path('download_file/<int:file_id>', controllers.download_file, name='file')
]
