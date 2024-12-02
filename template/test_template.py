import unittest
from template import template

class TestTemplate(unittest.TestCase):
	def test_template(self):
		expected_output = "Template"
		result = template()
		self.assertEqual(result, expected_output)


if __name__ == '__main__':
	unittest.main()
