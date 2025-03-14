from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateAPIView , DestroyAPIView
from .models import Menu
from .serializers import MenuItemSerializer

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateAPIView , DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})