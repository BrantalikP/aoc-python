
def day2(file_name):
	with open(file_name, 'r') as f:
		data = f.read().splitlines()
	cal = 0
	for i in data:
		value = isSafe(i)
		if value == True:
			cal += 1
	return cal

def isSafe(string: str) -> bool:
	nums = string.split(' ')
	isDecreasing = None
	for i in range(len(nums) - 1):
		next_number = int(nums[i + 1])
		current = int(nums[i])
		if abs(current - next_number) > 3 or abs(current - next_number) < 1:
			return False
		if current > next_number:
			if isDecreasing == None:
				isDecreasing = 0
			if isDecreasing != 0:
				return False

		if current < next_number:
			if isDecreasing == None:
				isDecreasing = 1
			if isDecreasing != 1:
				return False
	return True





if __name__ == '__main__':
	result = day2("data.txt")
	print("Result for day2", result)
