from django.test import TestCase

# Test Models
from .models import Menu;
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100);
        item_str = item.get_item();
        self.assertEqual(item_str, "IceCream (100) @ $80");
