import laba1matrix
import numpy as np
from datetime import datetime
import time


def nump(matrixnp):
	choice2 = input("Выберете действие:\n  1 - Возвести в квадрат \n  2 - Транспонировать \n  3 - Найти определитель(только для квадратной) \nВаш выбор: ")
	try:
		if choice2 == '1':
			start_time = datetime.now()
			ans = matrixnp * matrixnp
			print("-"*20, "\nВаша матрица возведённая в квадрат: \n",ans)
			print('\n   Прошло времени : ', datetime.now() - start_time)
		if choice2 == '2':
			start_time = datetime.now()
			print("-"*20, "\nВаша транспонированная матрица: \n",matrixnp.T)
			print('\n   Прошло времени : ', datetime.now() - start_time)
		if choice2 == '3':
			start_time = datetime.now()
			print("-"*20, "\nВаша определитель матрицы: \n",np.linalg.det(matrixnp))
			print('\n   Прошло времени : ', datetime.now() - start_time)
	except:
		print('-'*20,'\nЭто нельзя сделать для вашей матрицы!\n','-'*20)
		nump(matrixnp)
	repeat = input('\nХотите ещё действия с этой матрицей? \n')
	print()
	if repeat == 'да' or repeat == '+':
		nump(matrixnp)


def programm():
	print('-'*20,'\nВыберете способ выполнения\n  1 - С использованием NumPy\n  2 - Без использование NumPy')
	choice = input("Ваш выбор: ")
	if choice == '2':
		print('\n','-'*15,'Выполнение программы без NumPy','-'*15)
		laba1matrix.run(matrix)
	elif choice == '1':
		print('\n','-'*15,'Выполнение программы через NumPy','-'*15)
		nump(matrixnp)
		
if __name__ == '__main__':
	matrix = laba1matrix.create_matrix()
	matrixnp = np.array(matrix)
	programm()
	
#	 Без 	     С
# 1 - 00.00302  - 00.00502
# 2 - 00.00147  - 00.00615
# 3 - 00.00143  - 00.00299
