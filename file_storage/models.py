from django.db import models
from django.utils.safestring import mark_safe

from custom_users.models import MyUser
from web_secrets.settings import PATH_TO_USERS_FILES


class File(models.Model):
    user = models.ForeignKey(MyUser,
                             on_delete=models.CASCADE)
    filename = models.CharField(max_length=64,
                                blank=True)
    filesize = models.FloatField()
    upload_date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=PATH_TO_USERS_FILES)

    def __str__(self):
        return '; '.join((self.user.login,
                          self.filename,
                          str(self.filesize) + 'MB',))

    def fieldname_download(self):
        return mark_safe('<a href="/download_file/{0}">{1}</a>'
                         .format(self.id, self.filename))

    fieldname_download.short_description = 'Завантажений файл'

