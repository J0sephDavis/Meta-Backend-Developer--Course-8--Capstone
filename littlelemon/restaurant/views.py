from django.shortcuts import render
from rest_framework.serializers import ModelSerializer;
from rest_framework import generics;
from rest_framework.viewsets import *;
from .models import *;
from .serializers import *;
from rest_framework.permissions import *;
def index(request):
    return render(request, 'index.html',{});

class MenuItemView(generics.ListCreateAPIView):
    queryset=Menu.objects.all();
    serializer_class = MenuItemSerializer;

class SingleMenuItemView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset=Menu.objects.all();
    serializer_class = MenuItemSerializer;
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all();
    serializer_class = BookingSerializer;
    permission_classes=[IsAuthenticated];