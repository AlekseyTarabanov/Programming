import numpy as np
import random

def run():
	n = int(input('Введите n: '))
	if n < 6:
		print('Введите n больше 6, т.к. из матрицы должны быть удаленны 10 значений')
		run()
	else:
		tabl = np.random.randint(1,30,(n,n))
		print('Ваша матрица',n,'x',n,':')
		print(tabl) 
		delete_list = []
		c = 0
		print()
		while c != 10:
			deleteL = random.randint(0,n-1)
			deleteP = random.randint(0,n-1)
			if [deleteL,deleteP] in delete_list:
				continue
			else:
				c += 1
				delete_list.append([deleteL,deleteP])
				tabl[deleteL, deleteP] = 0
		print('Список удалённых индексов',delete_list)
		print('-'*25,'\n',tabl)
		
if __name__ == '__main__':
	print("Будет создана матрица n x n с диапозоном значений: от 1 до 30")
	run()
