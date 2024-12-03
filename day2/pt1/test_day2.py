import unittest
from day2 import isSafe

class TestTemplate(unittest.TestCase):
	def test_template(self):
		safe_int = "7 6 4 2 1"
		unsafe_int = '1 2 7 8 9'
		safe_result = isSafe(safe_int)
		unsafe_result = isSafe(unsafe_int)
		print("THIS IS MINE", safe_result)
		self.assertEqual(safe_result, True)
		self.assertEqual(unsafe_result, False)


if __name__ == '__main__':
	unittest.main()
