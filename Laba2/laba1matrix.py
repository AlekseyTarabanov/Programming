from datetime import datetime
import time

def create_matrix():
	count_stolb = int(input("Введите ко-во столбцов: "))
	count_str = int(input("Введите ко-во строк: "))
	count_a = 0
	a_list = []
	matrix = []
	for i in range(count_str):
		a_list = []
		matrix.append(a_list)
		for j in range(count_stolb):
			count_a += 1
			A = "A" + str(count_a)
			a_list.append(A)
		print(a_list)

	count_a = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			count_a += 1
			matrix[i][j] = int(input("Введите значение "+"A"+str(count_a)+": "))
	print("-"*20, "\nВаша матрица:")
	for i in range(len(matrix)):
		print(matrix[i])
	return matrix
	
def kvadrat(matrix):
	K_matrix = []
	for i in range(len(matrix)):
		K_line = []
		for j in range(len(matrix[i])):
			K_line.append(0)
		K_matrix.append(K_line)
	for i in range(len(matrix)):  
		for j in range(len(matrix[i])): 
			for z in range(len(matrix)):  
				K_matrix[i][j] += int(matrix[i][z]) * int(matrix[z][j])
	return K_matrix
	
def transpon(matrix):
	T_matrix = []
	for i in range(len(matrix)):
		T_line = []
		for j in range(len(matrix[i])):
			T_line.append(matrix[j][i])
		T_matrix.append(T_line)
	return T_matrix
	
def opredel(matrix):
	if len(matrix) == 2:
		return int(matrix[0][0]) * int(matrix[1][1]) - int(matrix[0][1]) * int(matrix[1][0])
	else:
		O_matrix = 0
		for i in range(len(matrix)):
			O_matrix1 = []
			for j in range(1, len(matrix)):
				O_line = []
				for k in range(len(matrix[j])):
					if k != i:
						O_line.append(matrix[j][k])
				O_matrix1.append(O_line)
			O_matrix += int(matrix[0][i]) * (-1) ** ((i + 1) + (0 + 1)) * opredel(O_matrix1)
	return O_matrix

def run(matrix):
	vibor = int(input("Выберете действие:\n  1 - Возвести в квадрат \n  2 - Транспонировать \n  3 - Найти определитель(только для квадратной) \nВаш выбор: "))
	if vibor != 1 and vibor != 2 and vibor != 3:
		print("Вы выбрали что-то не то)")
	elif vibor == 1:
		countS, countL = 0, 0
		for i in range(len(matrix)):
			countS += 1
			countL = 0
			for j in range(len(matrix[i])):
				countL += 1
		if countL == countS:
			start_time = datetime.now()
			print("-"*20, "\nВаша матрица возведённая в квадрат: ")
			for i in range(len(kvadrat(matrix))):
				print(kvadrat(matrix)[i])
			print('\n   Прошло времени : ', datetime.now() - start_time)
		else:
			print("Ваша матрица не может быть возведена в квадрат")
	elif vibor == 2:
		countS, countL = 0, 0
		for i in range(len(matrix)):
			countS += 1
			countL = 0
			for j in range(len(matrix[i])):
				countL += 1
		if countL == countS:
			start_time = datetime.now()
			print("-"*20, "\nВаша транспонированная матрица: ")
			for i in range(len(transpon(matrix))):
				print(transpon(matrix)[i])
			print('\n   Прошло времени : ', datetime.now() - start_time)
		else:
			print("Ваша матрица не квадратная")
	elif vibor == 3:
		countS, countL = 0, 0
		for i in range(len(matrix)):
			countS += 1
			countL = 0
			for j in range(len(matrix[i])):
				countL += 1
		if countL == countS:
			start_time = datetime.now()
			print("-"*20, "\nВаш детрименант матрицы: ")
			print(opredel(matrix))
			print('\n   Прошло времени : ', datetime.now() - start_time)
		else:
			print("Ваша матрица не квадратная")
	repeat = input('\nХотите ещё действия с этой матрицей? \n')
	print()
	if repeat == 'да' or repeat == '+':
		run(matrix)

if __name__ == '__main__':
	matrix = create_matrix()
	run(matrix)
