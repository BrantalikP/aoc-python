

def lookHorizontal(array):
	total = 0
	for index, i in enumerate(array):
		total += sum(1 for t,a,b,c in zip(i, i[1:],i[2:], i[3:]) if t + a + b + c == 'XMAS')
	return total

def lookVertical(array):
	total = 0
	for i in range(len(array[0])):
		for k in range(len(array) - 3):
			first = array[k][i]
			second = array[k + 1][i]
			third = array[k + 2][i]
			forth = array[k + 3][i]
			if first + second + third + forth == 'XMAS':
				total += 1
	return total


def lookDiagonal(array):
	total = 0
	for i in range(len(array) - 3):
		for k in range(len(array[0]) - 3):
			first = array[i][k]
			second = array[i + 1][k + 1]
			third = array[i + 2][k + 2]
			forth = array[i + 3][k + 3]
			if first + second + third + forth == 'XMAS':
				total += 1
	return total


def revertList(array):
	reversed_list = list(reversed(array))
	reversed_map = [list(reversed(sublist)) for sublist in reversed_list]
	return reversed_map


def createMap(ar: list[str]):
	map = []
	for index, i in enumerate(ar):
		map.append(list(i))
	return map



def main(file_name):
	file = read_file(file_name)
	map = createMap(list(file))
	rev = revertList(map)
	horizontal = lookHorizontal(map)
	horizontal_rev = lookHorizontal([list(reversed(sublist)) for sublist in map])
	vertical = lookVertical(map)
	vertical_rev = lookVertical(list(reversed(map)))
	diagonal = lookDiagonal(map)
	diagonal_right = lookDiagonal([list(reversed(sublist)) for sublist in map])
	diagonal_ver = lookDiagonal(list(reversed(map)))
	diagonal_ver_rev = lookDiagonal(rev)

	return diagonal_right + vertical_rev + horizontal + horizontal_rev + vertical + diagonal + diagonal_ver + diagonal_ver_rev





def read_file(file_name):
	with open(file_name, 'r') as f:
		return f.read().splitlines()


if __name__ == '__main__':
	result = main("data.txt")
	print("Result:", result)
