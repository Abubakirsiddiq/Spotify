from unittest import TestCase
from rest_framework.test import APIClient


# class TestQoshiqchi(TestCase):
#     def setUp(self) -> None:
#         self.client=APIClient()
#     def test_qoshiqchi(self):
#         natija=self.client.get("/qoshiqchi/2/")
#         assert natija.status_code==200
#         assert natija.data["id"]==2
#     def test_qoshiqchi_invalid(self):
#         natija = self.client.get("/qoshiqchi/3/")
#         assert natija.status_code == 404
    # def test_qoshiqchi_post(self):
        # malumot={"ism":"Shoxjahon Jorayev", "mamlakat":"Ozbekiston","janr":"Mumtoz"}
        # natija=self.client.post("/qoshiqchilar/",data=malumot)
        # assert natija.status_code==201
    # def test_qoshiqchi_put(self):
    #     malumot={"ism":"Shoxjahon Jorayev", "mamlakat":"Ozbekiston","janr":"Mumtoz"}
    #     natija=self.client.put("/qoshiqchi/2/", data=malumot)
    #     assert natija.status_code==200
    #     assert natija.data["id"]==2


# class TestAlbom(TestCase):
#     def setUp(self) -> None:
#         self.client=APIClient()

