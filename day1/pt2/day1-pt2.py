
def calculate_similarity(data):
	groupA, groupB = data
	total = 0
	for i in range(len(groupA)):
		occur = 0

		for l in range(len(groupB)):
			if groupA[i] == groupB[l]:
				occur += 1
		total += int(groupA[i]) * occur
	return total



def group_data(data):
	groupA = []
	groupB = []
	for i in data:
		split_data = i.split(' ')
		groupA.append(split_data[0])
		groupB.append(split_data[len(split_data)-1])
	return groupA, groupB

def day1(file_name):
	with open(file_name, 'r') as f:
		data = f.read().splitlines()
	grouped = group_data(data)
	result = calculate_similarity(grouped)
	print("Solution for Day1:", result)



if __name__ == '__main__':
	day1('data.txt')
