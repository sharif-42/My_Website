from django.test import TestCase

from .models import User


class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        user = User.objects.create_user(username='Sharif', password='sharif123')
        print('User: {} Password: {}'.format(user.username, user.password))
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(self):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         user = User.objects.create_user(username='Sharif', password='sharif123')
#         print('User: {} Password: {}'.format(user.username, user.password))
#
#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass
#
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)
#
#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)
#
#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)
