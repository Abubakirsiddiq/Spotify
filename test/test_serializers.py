from unittest import TestCase
from music.models import Albom,Qoshiqchi,Qoshiq
from music.serializers import AlbomSerializer,QoshiqSerializer


# class TestAlbom(TestCase):
#     def setUP(self):
#         # Albom.objects.create(
#         #         nom="Qoshiqlar",
#         #         sana="2020-05=10",
#         #         qoshiqchi=Qoshiqchi.objects.last()
#         #     )
#         self.albom=Albom.objects.last()
#     def test_albom(self):
#         s=AlbomSerializer(self.albom)


# class TestQoshiq(TestCase):
#     def setUP(self):
#         Qoshiq.objects.create(
#                 nom="Dunyo seni togang mas",
#                 eshitish_soni=100,
#                 albom=Albom.objects.last(),
#                 fayl="dunyo.mp3"
#             )
#         self.qoshiq=Qoshiq.objects.last()
#     def test_qoshiq(self):
#         s=QoshiqSerializer(self.qoshiq)

