from django.test import TestCase
from .models import Brand, CarModel, CarOption, SpecificCarOption
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone
import redgreenunittest as unittest

class AssociationTestCase(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create()
        self.car_model = CarModel.objects.create(brand=self.brand)
        self.order = Order.objects.create(user=self.user, restaurant=self.restaurant)
        self.car_option_1 = CarOption.objects.create()
        self.car_option_2 = CarOption.objects.create()
        self.car_option_3 = CarOption.objects.create()
        self.car_option_4 = CarOption.objects.create()
        self.specific_car_option_1 = SpecificCarOption.objects.create(order=self.order, food_item=self.food_item_1)
        self.order_food_item_2 = OrderFoodItem.objects.create(order=self.order, food_item=self.food_item_2)
        self.order_food_item_3 = OrderFoodItem.objects.create(order=self.order, food_item=self.food_item_3)
        self.order_food_item_4 = OrderFoodItem.objects.create(order=self.order, food_item=self.food_item_4)

    def test_01_user_orders(self):
        """returns the user's orders"""
        self.assertEqual(list(self.user.orders.all()),[self.order])

    def test_02_orders_user(self):
        """returns the order's user"""
        self.assertEqual(self.order.user, self.user)

    def test_03_restaurant_orders(self):
        """returns the restauants orders"""
        self.assertEqual(list(self.restaurant.orders.all()), [self.order])

    def test_04_order_restaurant(self):
        """returns the order's restaurant"""
        self.assertEqual(self.order.restaurant, self.restaurant)

    def test_05_orders_food_items(self):
        """returns the order's food items"""
        self.assertEqual(list(self.order.food_items.all()), [self.food_item_1, self.food_item_2, self.food_item_3, self.food_item_4])

    def test_06_food_item_orders(self):
        """returns all orders that contain the food item"""
        self.assertEqual(list(self.food_item_1.orders.all()), [self.order])
        self.assertEqual(list(self.food_item_2.orders.all()), [self.order])
        self.assertEqual(list(self.food_item_3.orders.all()), [self.order])
        self.assertEqual(list(self.food_item_4.orders.all()), [self.order])

    def test_07_users_food_items(self):
        """returns all the food items in the order"""
        all_food_items = list(list((order.food_items.all()) for order in list(self.user.orders.all()))[0])
        self.assertEqual(all_food_items, [self.food_item_1, self.food_item_2, self.food_item_3, self.food_item_4])



    record = SwimRecord()

    def test_01_validate_first_name_presence(self):
        new_user = SwimRecord(first_name='', last_name='Prete', team_name='beavers')
        try:
            self.record.full_clean()
            raise Exception("full_clean should throw a validation error")
        except ValidationError as e:
            self.assertTrue('This field cannot be blank.' in e.message_dict['first_name'])

    def test_02_validate_last_name_presence(self):
        new_user = SwimRecord(first_name='Tom', last_name='', team_name='beavers')
        try:
            self.record.full_clean()
            raise Exception("full_clean should throw a validation error")
        except ValidationError as e:
            self.assertTrue('This field cannot be blank.' in e.message_dict['last_name'])

    def test_03_validate_team_name_presence(self):
        new_user = SwimRecord(first_name='Tom', last_name='Prete', team_name='')
        try:
            self.record.full_clean()
            raise Exception("full_clean should throw a validation error")
        except ValidationError as e:
            self.assertTrue('This field cannot be blank.' in e.message_dict['team_name'])

    def test_04_validate_relay_presence(self):
        new_user = SwimRecord(first_name='Tom', last_name='Prete', team_name='beavers', relay='')
        try:
            self.record.full_clean()
            raise Exception("full_clean should throw a validation error")
        except ValidationError as e:
            self.assertTrue("'None' value must be either True or False." in e.message_dict['relay'])

    def test_05_valid_stroke(self):
        """validates that the stroke is one of 'front crawl', 'butterfly', 'breast', 'back', or 'freestyle'"""
        stroke_record = SwimRecord(stroke='doggie paddle')
        try:
            stroke_record.full_clean()
            raise Exception("full_clean should throw a validation error")
        except ValidationError as e:
            self.assertTrue("doggie paddle is not a valid stroke" in e.message_dict['stroke'])

    def test_06_valid_distance(self):
        """must be greater than or equal to 50"""
        distance_record = SwimRecord(distance=20)
        try:
            distance_record.full_clean()
            raise Exception("full_clean should throw a validation error")
        except ValidationError as e:
            self.assertTrue("Ensure this value is greater than or equal to 50." in e.message_dict['distance'])

    def test_07_no_future_records(self):
        """does not allow records to be set in the future"""
        bad_date = timezone.now() + timedelta(days=1)
        record = SwimRecord(record_date=bad_date)
        try:
            record.full_clean()
            raise Exception("full_clean should throw a validation error")
        except ValidationError as e:
            self.assertTrue("Can't set record in the future." in e.message_dict['record_date'])

    def test_08_no_break_record_before_set_record(self):
        """does not allow records to be broken before the record_date"""
        record = SwimRecord(first_name='j',last_name='j',team_name='k',relay=True,stroke='butterfly',distance=100,record_date=timezone.now(),record_broken_date=(timezone.now() - timedelta(days=1)))
        record.save()
        try:
            record.full_clean()
            raise Exception("full_clean should throw a validation error")
        except ValidationError as e:
            self.assertTrue("Can't break record before record was set." in e.message_dict['record_broken_date'])
