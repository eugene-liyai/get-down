from unittest import TestCase
import views

class ModelTestClass(TestCase):

	def test_category(self):

		self.assertIsInstance(list, views.new_category(2))