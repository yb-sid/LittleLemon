from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateAPIView , DestroyAPIView
from .models import Menu , Booking
from .serializers import MenuItemSerializer , BookingSerialzer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateAPIView , DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerialzer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})