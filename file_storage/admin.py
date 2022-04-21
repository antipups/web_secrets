from django.contrib import admin
from file_storage.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    readonly_fields = ('fieldname_download', )
