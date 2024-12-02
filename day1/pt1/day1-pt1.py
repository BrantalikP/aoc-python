
def calculate_distance(data):
	groupA, groupB = data
	distance = 0
	for i in range(len(groupA)):
		distance += abs(int(groupA[i]) - int(groupB[i]))
	return distance


def group_data(data):
	groupA = []
	groupB = []
	for i in data:
		split_data = i.split(' ')
		groupA.append(split_data[0])
		groupB.append(split_data[len(split_data)-1])
	return sorted(groupA), sorted(groupB)

def day1(file_name):
	with open(file_name, 'r') as f:
		data = f.read().splitlines()
	grouped = group_data(data)
	result = calculate_distance(grouped)
	print("Solution for Day1:", result)



if __name__ == '__main__':
	day1('data.txt')
