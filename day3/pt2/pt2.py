import re

pattern = r"mul\((\d+),\s*(\d+)\)"

def filterDont(text: str):
	dont_pattern = r"don't\(\)(.*?)(do\(\)|$)"
	return re.sub(dont_pattern, '', text)

def read_file(file_name):
	with open(file_name, 'r') as file:
		return file.read().replace("\n", "")


def find_numbers(text: str):
	matches = re.findall(pattern, text)
	return matches


def main(file_name):
	text = read_file(file_name)
	filtered_text = filterDont(text)
	matches = find_numbers(filtered_text)
	return sum(int(num1) * int(num2) for num1, num2 in matches)


if __name__ == '__main__':
	result = main("data.txt")
	print("Result:", result)
