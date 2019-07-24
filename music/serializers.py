from rest_framework import serializers
import os
from .models import Musics

class MusicsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Musics
        fields = ('id','nama_lagu', 'nama_artis', 'link_audio', 'duration')

    def create(self, validated_data):

        file = Musics(
            nama_lagu=validated_data['nama_lagu'],
            nama_artis=validated_data['nama_artis'],
            link_audio=validated_data['link_audio']
        )
        file.save()
        return file
