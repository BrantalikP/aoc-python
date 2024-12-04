import unittest
from pt2 import main

class TestTemplate(unittest.TestCase):
	def test_main(self):
		result = main('test_data.txt')
		self.assertEqual(result, 0)


if __name__ == '__main__':
	unittest.main()
