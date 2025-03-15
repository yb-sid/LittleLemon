from django.test import TestCase
from django.urls import reverse
from ..models import Menu
from ..serializers import MenuItemSerializer
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        """Create test instances of the Menu model."""
        self.item1 = Menu.objects.create(title="Pasta", price=12.99, inventory=10)
        self.item2 = Menu.objects.create(title="Pizza", price=15.99, inventory=5)
        self.item3 = Menu.objects.create(title="Salad", price=8.99, inventory=20)
        
        self.client = APIClient()
    
    def test_getall(self):
        """Retrieve all Menu objects and check if serialized data matches response."""
        response = self.client.get(reverse('menu-list'))  # menu-list is the url name
        
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
