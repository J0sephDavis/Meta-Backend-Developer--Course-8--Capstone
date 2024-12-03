from typing import List;
from django.test import TestCase
from .models import Menu;

# Test Models
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100);
        item_str = item.get_item();
        self.assertEqual(item_str, "IceCream : 80");

class MenuViewTest(TestCase):
    product_name:List[str] = ["Ice Cream", "Pasta"];
    product_prices:List[float] = [10.99,100.00];
    product_inventory:List[int] = [10,20];
    
    def setUp(self):
        for name in self.product_name:
            for price in self.product_prices:
                for inventory in self.product_inventory:
                    m = Menu.objects.create(title=name, price=price, inventory=inventory);

    def test_getall(self):
        for name in self.product_name:
            for price in self.product_prices:
                for inventory in self.product_inventory:
                    item = Menu.objects.get(title=name, price=price, inventory=inventory);
                    self.assertEqual(item.get_item(), "{} : {:.2f}".format(name,price));