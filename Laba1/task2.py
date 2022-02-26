#1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4, -5, -6, 0, -0, 1.5, 1.25, -99.9999, e, P

def perevod(num, num_list):
	b = ""
	for i in num:
		if "0" <= i <= "9" or i == "-" or i == "." or i == "P" or i == "e":	
			b += i
		elif i == ",":
			num_list.append(b)
			b = ""
	num_list.append(b)
	return(num_list)


# поиск натуральных чисел
def task2(num_list):
	num_nat = []
	for i in num_list:
		if i.isnumeric():
			num_nat.append(int(i))
	print("\nНатуральные числа: ", num_nat)

	# поиск целых чисел

	num_cel = []
	for i in num_list:
		if i.isdigit() or i[1:].isdigit():
			num_cel.append(int(i))
	print("Целые числа: ", num_cel)

	# поиск рациональных чисел

	num_rac = []
	for i in num_list:
		if i.isdigit() or i[1:].isdigit():
			num_rac.append(int(i))
		elif i != "P" and i != "e":
			num_rac.append(float(i))
	print("Рациональные числа: ", num_rac)

	# поиск вещественных чисел

	num_vec = []
	for i in num_list:
		if i.isdigit() or i[1:].isdigit():
			num_vec.append(int(i))
		elif i == "P" or i == "e":
			num_vec.append(i)
		else:
			num_vec.append(float(i))
	print("Вещественные числа: ", num_vec)

	# поиск чётных чисел

	num_chet = []
	for i in num_list:
		if (i.isdigit() or i[1:].isdigit()):
			if int(i) % 2 == 0 and int(i) != 0:
				num_chet.append(int(i))
	print("Чётные числа: ", num_chet)

	# поиск нечётных чисел

	num_nechet = []
	for i in num_list:
		if (i.isdigit() or i[1:].isdigit()):
			if int(i) % 2 != 0 and int(i) != 0:
				num_nechet.append(int(i))
	print("Нечётные числа: ", num_nechet)

	# поиск простых чисел

	num_pro = []
	count_del = 0
	for i in num_nat:
		for j in range(2, i):
			if i % j == 0:
				count_del = count_del + 1
		if count_del == 0:
			num_pro.append(i)
		else:
			count_del = 0

	print("Простые числа: ", num_pro)
	
if __name__ == '__main__':
	num = input()
	num_list = []
	task2(perevod(num, num_list))
