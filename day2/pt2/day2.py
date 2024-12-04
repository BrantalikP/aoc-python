
def day2(file_name):
	with open(file_name, 'r') as f:
		data = f.read().splitlines()
	return sum(1 for line in data if recursiveSafe(line))


def recursiveSafe(string: str):
	nums = string.split(' ')
	if isSafe(nums):
		return True
	return any(isSafe(nums[:i] + nums[i+1:]) for i in range(len(nums)))

def isSafe(nums: list[int]) -> bool:
	isDecreasing = None
	for current, next_number in zip(nums, nums[1:]):
		if not 1 <= abs(current - next_number) <= 3:
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
