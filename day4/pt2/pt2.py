


def lookDiagonal(array, rev: bool):
	total = list()

	for i in range(len(array) - 2):
		for k in range(len(array[0]) - 2):
			first = array[i][k]
			second = array[i + 1][k + 1]
			third = array[i + 2][k + 2]
			if first + second + third == 'MAS' or first + second + third == 'SAM':
				if rev:
					total.append(f"{(i + 1)}:{len(array[0]) - 1 - (k + 1)}")
				else:
					total.append(f"{i + 1}:{k + 1}")
	return total



def createMap(ar: list[str]):
	map = []
	for index, i in enumerate(ar):
		map.append(list(i))
	return map



def main(file_name):
	file = read_file(file_name)
	map = createMap(list(file))

	diagonal = lookDiagonal(map, False)
	diagonal_ver = lookDiagonal([list(reversed(sublist)) for sublist in map], True)
	set1 = set(diagonal)
	set2 = set(diagonal_ver)

	matches = set1 & set2

	return len(matches)


def read_file(file_name):
	with open(file_name, 'r') as f:
		return f.read().splitlines()


if __name__ == '__main__':
	result = main("data.txt")
	print("Result:", result)
