from rest_framework import generics
from cars.serializers import CarDetailSerializer
from cars.models import Car


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
