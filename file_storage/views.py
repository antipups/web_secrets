from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from file_storage.models import File
from web_secrets import settings


class FileList(LoginRequiredMixin, ListView):
    model = File
    paginate_by = 20
    template_name = 'file_storage/file_list.html'
    context_object_name = 'files'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super(FileList, self).get_context_data()
        context_data['max_file_size'] = settings.MAX_FILE_SIZE
        context_data['auth'] = True
        return context_data

