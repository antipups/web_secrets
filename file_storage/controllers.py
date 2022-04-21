from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect
from django.http.response import HttpResponse, FileResponse

from file_storage.models import File


def load_file(request: WSGIRequest):
    file = request.FILES['file_load']
    File(user=request.user,
         file=file,
         filename=file.name,
         filesize=round(file.size / 1024 / 1024, 2)).save()
    return redirect('file_storage:file_list')


def download_file(request: WSGIRequest, file_id: int):
    if files := File.objects.filter(id=file_id):
        file = files[0]
        if request.user.is_admin or file.user == request.user:
            return FileResponse(open(file.file.name, 'rb'),
                                filename=file.filename)

    return HttpResponse(status=404)
