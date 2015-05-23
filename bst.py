def bst(r,i,j,key):
	if (i==j):
		return False;
	mid = (i+j)/2
	if r[mid] == key:
		return True;
	elif r[mid] > key:
		return bst(r,i,mid-1,key)
	else:
		return bst(r,mid+1,j,key)
def testBst(r,key,res):
	if bst(r,0,len(r),key) == res:
		print 'SUCCESS'
	else:
		print 'FAIL'
		exit(-1)

r = range(1,10)
testBst(r,5,True)
testBst(r,12,False)