from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from tinytag import TinyTag
from django.conf import settings
import os
import datetime

class Musics(models.Model):
    nama_lagu = models.CharField(max_length=255)
    nama_artis = models.CharField(max_length=255)
    link_audio = models.FileField(upload_to='musics', blank=False, null=False, unique=True)
    durasi_audio = models.FloatField(editable=False, default=0)
    
    def duration(self):
        file_path = os.path.join(settings.MEDIA_ROOT, self.link_audio.name)
        tag = TinyTag.get(file_path)
        return str(datetime.timedelta(seconds=tag.duration))

    def save(self, *args, **kwargs):
        super(Musics, self).save(*args, **kwargs)
        file_path = os.path.join(settings.MEDIA_ROOT, self.link_audio.name)
        tag = TinyTag.get(file_path)
        file_extension = os.path.splitext(file_path)[1]
        if file_extension == '.mp3':
            self.durasi_audio = tag.duration
            super(Musics, self).save(*args, **kwargs)
    
    def __str__(self):
        return "{} - {}".format(self.nama_lagu, self.nama_artis)

@receiver(post_delete, sender=Musics)
def submission_delete(sender, instance, **kwargs):
    instance.link_audio.delete(False) 