import unittest
from day2 import recursiveSafe

class TestTemplate(unittest.TestCase):
	def test_safe_cases(self):
		safe_cases = ["7 6 4 2 1", "1 3 2 4 5"]

		for case in safe_cases:
			with self.subTest(case):
				result = recursiveSafe(case)
				self.assertEqual(result, True,f"Failed on safe case: {case}")

	def test_unsafe_cases(self):
		unsafe_cases = ["1 2 7 8 9", "9 7 6 2 1"]

		for case in unsafe_cases:
			with self.subTest(case):
				result = recursiveSafe(case)
				self.assertEqual(result, False,f"Failed on unsafe case: {case}")


if __name__ == '__main__':
	unittest.main()
