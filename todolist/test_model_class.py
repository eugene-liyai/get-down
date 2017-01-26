from unittest import TestCase
from views import db
from models import Category, User

class ModelTestClass(TestCase):

	def test_return_list(self):
		self.assertIsInstance(Category, type(Category.get_by_catid(1)))

	def test_user(self):
		self.assertEqual(User.username, User.get_by_username('liyai'))

	def test_user(self):
		self.assertTrue(True, Task.get_by_taskid(1))