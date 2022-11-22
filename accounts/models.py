from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime

from cloudinary.models import CloudinaryField

# Create your models here.

class Audio(models.Model):

    name = models.CharField(max_length=200,null=True)
    #message = models.TextField(null=True)
    date_created = models.DateTimeField(default=timezone.now(), blank=False)
    file = CloudinaryField(resource_type='video',null=True, blank=True, folder='kin-keepers/')
    message  = CloudinaryField(resource_type='raw',null=True,folder='transcriptions/')



    def __str__(self) -> str:
        return str(self.file)
