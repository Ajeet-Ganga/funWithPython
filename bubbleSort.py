import random
def bubbleSort(arr):
	if arr is None:
		return
	if len(arr) == 0:
		return
	if len(arr) == 1:
		return
	for (i,j) in [(i,j) for i in range(0,len(arr)) for j in range(i+1,len(arr))] :
		# print i,j,arr[i],arr[j]
		if (arr[i] > arr[j]):
			# print 'swap',i,j
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
def test(arr):
	print arr
	bubbleSort(arr)
	print arr
	for i in range(0,len(arr)-2):
		if arr[i] > arr[i+1] : 
			print 'FAIL'
			exit(-1)
	print 'SUCCESS'



arr = random.sample(range(0,99),50)
test(arr)


