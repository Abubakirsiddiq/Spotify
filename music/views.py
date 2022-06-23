from rest_framework import status
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class HelloAPI(APIView):
    def get(self, request):
        data = {"xabar": "Birinchi API yaratildi!"}
        return Response(data)

    def post(self, request):
        data = request.data()
        return Response(data)


class QoshiqchilarAPIView(APIView):
    def get(self, request):
        qoshiqchilar = Qoshiqchi.objects.all()
        serializer = QoshiqchiSerializer(qoshiqchilar, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        ser = QoshiqchiSerializer(data=malumot)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)


class QoshiqchiAPIView(APIView):
    def get(self, request, pk):
        # qoshiqchi = Qoshiqchi.objects.get(id=pk)
        qoshiqchi = get_object_or_404(Qoshiqchi, id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi)
        return Response(serializer.data)

    def put(self, request, pk):
        qoshiqchi = get_object_or_404(Qoshiqchi, id=pk)
        ser = QoshiqchiSerializer(qoshiqchi, request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)

    def patch(self, request, pk):
        qoshiqchi = get_object_or_404(Qoshiqchi, id=pk)
        ser = QoshiqchiSerializer(qoshiqchi, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        try:
            get_object_or_404(Qoshiqchi, id=pk).delete()
            data = {"xabar":"Muvaffaqiyatli o'chirildi!"}
            return Response(data, status=status.HTTP_200_OK)
        except:
            data = {"xabar":"Bu id'da qo'shiqchi yo'q!"}
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class AlbomlarAPIView(APIView):
    def get(self, request):
        albomlar = Albom.objects.all()
        serializer = AlbomSerializer(albomlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        ser = AlbomSerializer(data=malumot)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)


class AlbomAPIView(APIView):
    def get(self, request, pk):
        albom = Albom.objects.get(id=pk)
        serializer = AlbomSerializer(albom)
        return Response(serializer.data)

    def put(self, request, pk):
        albo = Albom.objects.get(id=pk)
        ser = AlbomSerializer(albo, request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)


class QoshiqlarAPIView(APIView):
    def get(self, request):
        qoshiqlar = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        ser = QoshiqSerializer(data=malumot)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)


