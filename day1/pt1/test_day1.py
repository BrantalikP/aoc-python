import unittest
from template import template

class TestTemplate(unittest.TestCase):
	def test_day1(self):
		expected_output = "Template"
		result = template()
		self.assertEqual(result, expected_output)


if __name__ == '__main__':
	unittest.main()
