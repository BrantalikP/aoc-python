import re

pattern = r"mul\((\d+),\s*(\d+)\)"

def read_file(file_name):
	with open(file_name, 'r') as file:
		return file.read()


def find_numbers(text: str):
	matches = re.findall(pattern, text)
	return matches


def main(file_name):
	text = read_file(file_name)
	matches = find_numbers(text)
	return sum(int(num1) * int(num2) for num1, num2 in matches)


if __name__ == '__main__':
	result = main("data.txt")
	print("Result:", result)
