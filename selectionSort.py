import random
def selSort(arr):
	if arr is None:
		return
	if len(arr) == 0:
		return
	if len(arr) == 1:
		return
	for i in range(0,len(arr)-1):
		min = arr[i]
		minI = i
		for j in range(i+1,len(arr)):
			if (min > arr[j]):
				min = arr[j]
				minI = j
		if i != minI:
			temp = arr[i]
			arr[i] = arr[minI]
			arr[minI] = temp
def test(arr):
	print arr
	selSort(arr)
	print arr
	for i in range(0,len(arr)-2):
		if arr[i] > arr[i+1] : 
			print 'FAIL'
			exit(-1)
	print 'SUCCESS'



arr = random.sample(range(0,99),50)
test(arr)


