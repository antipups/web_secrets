from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect

from file_storage.models import File


def load_file(request: WSGIRequest):
    file = request.FILES['file_load']
    File(user=request.user,
         file=file,
         filename=file.name,
         filesize=round(file.size / 1024 / 1024, 2)).save()
    return redirect('file_storage:file_list')
