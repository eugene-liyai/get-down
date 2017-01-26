from unittest import TestCase
from models import Category

class ModelTestClass(TestCase):

	def test_return_list(self):
		self.assertIsInstance(Category, type(Category.get_by_catid(1)))

	def test_user(self):
		user = User.get_by_username('liyai')
		self.assertEqual('liyai', user.username)

	def test_user(self):
		self.assertTrue(True, Task.get_by_taskid(1))