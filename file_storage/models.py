from django.db import models

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

