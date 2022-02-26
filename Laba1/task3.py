num = input("Введите массив чисел: ")
print("-" * 20)

# Запись чисел в массив

num_list = []
b = ""
for i in num:
	if "0" <= i <= "9" or i == "-":	
		b += i
	elif i == " ":
		num_list.append(int(b))
		b = ""
num_list.append(int(b))

# Пузырьковая сортировка	

num_buble = num_list
def buble_sort(num_buble):
	swapped = True
	while swapped == True:
		swapped = False
		for i in range(0, len(num_buble)-1):
			if num_buble[i] > num_buble[i+1]:
				num_buble[i], num_buble[i+1] = num_buble[i+1], num_buble[i]
				swapped = True 
	return num_buble
print("Пузырьковая сортировка: ", buble_sort(num_buble))

# Гномья сортировка

num_gnome = num_list
def gnume_sort(num_gnome):
	for i in range(0, len(num_gnome)-1):
		if num_gnome[i] > num_gnome[i+1]:
			num_gnome[i], num_gnome[i+1] = num_gnome[i+1], num_gnome[i]
			for j in range(i, 0, -1):
				if num_gnome[j] < num_gnome[j-1]:
					num_gnome[j], num_gnome[j-1] = num_gnome[j-1], num_gnome[j]
			gnume_sort(num_gnome)
	return num_gnome
print("Гномья сортировка: ", gnume_sort(num_gnome))

# Блочная сооортировка

num_bucket = num_list
def bucket_sort(num_bucket):
	max_value = max(num_bucket)
	min_num = min(num_bucket)
	max_num = max(num_bucket)
	size = max_num/len(num_bucket)
	buckets_list= []
	for x in range(len(num_bucket)):
		buckets_list.append([]) 
	for i in range(len(num_bucket)):
		j = int(num_bucket[i] / size)
		if j != len (num_bucket):
			buckets_list[j].append(num_bucket[i])
		else:
			buckets_list[len(num_bucket) - 1].append(num_bucket[i])

	for z in range(len(num_bucket)):
		buble_sort(buckets_list[z])
	final_output = []
	for x in range(len (num_bucket)):
		final_output = final_output + buckets_list[x]
	return final_output
print("Блочная сортировка: ", bucket_sort(num_bucket))

# Пирамидальная сортировка

num_heap = num_list
def heap_sort(alist):
    def parent(i):
        return (i - 1) // 2

    def left(i):
        return 2 * i + 1

    def right(i):
        return 2 * i + 2

    def max_heapify(alist, index, size):
        l = left(index)
        r = right(index)
        if (l < size and alist[l] > alist[index]):
            largest = l
        else:
            largest = index
        if (r < size and alist[r] > alist[largest]):
            largest = r
        if (largest != index):
            alist[largest], alist[index] = alist[index], alist[largest]
            max_heapify(alist, largest, size)

    def build_max_heap(alist):
        length = len(alist)
        start = parent(length - 1)
        while start >= 0:
            max_heapify(alist, index=start, size=length)
            start = start - 1

    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)

    return alist

print("Пирамидальная сортировка: ", heap_sort(num_heap))
