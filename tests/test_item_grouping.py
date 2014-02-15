from django.test import TestCase
from homepage.models import Item
from homepage.utils import group_items_by_dates
import datetime

class GroupItemsByDatesTestCase(TestCase):
    
    def setUp(self):
        
        # Two items in december 2012
        self.create_item(2012, 12, 1)
        self.create_item(2012, 12, 2)
        
        # Three items in March 2013
        self.create_item(2013, 3, 14)
        self.create_item(2013, 3, 1)
        self.create_item(2013, 3, 1)
        
        # One item in April 2013
        self.create_item(2013, 4, 20)

        self.grouped_items = group_items_by_dates(Item.objects.all())

    
    def test_number_of_groups_expected(self):
        
        self.assertEqual(len(self.grouped_items), 3)
        
    def test_each_group_has_expected_number_of_items(self):

        self.assertEqual(len(self.grouped_items["December 2012"]), 2)
        self.assertEqual(len(self.grouped_items["March 2013"]), 3)
        self.assertEqual(len(self.grouped_items["April 2013"]), 1)
        
    def test_correct_dates_in_group(self):
        
        self.verify_items_in_group("December 2012", 12, 2012)
        self.verify_items_in_group("March 2013", 3, 2013)
        self.verify_items_in_group("April 2013", 4, 2013)

    # Utilities
    # ---------
    
    def verify_items_in_group(self, group_name, correct_month, correct_year):
        for item in self.grouped_items[group_name]:
                self.assertEqual(item.date.month, correct_month)
                self.assertEqual(item.date.year, correct_year)
                
    def create_item(self, y, m, d):
        """ This simply creates an item on a particular day. """
        Item.objects.create(
            name="Item {0}{1}{2}".format(y,m,d), 
            date=datetime.date(y,m,d),
            project_id=0)
