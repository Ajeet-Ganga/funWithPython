import string
import sys
from collections import deque
'''
NODE = CHAR (Node)* '#'
CHAR = (A-Z){1}

e.g.
A#	=>	_A_ _None_ '#'
AB##	=>	_A_ _B_ _None_ '#' '#' 

'''
class N:
	v = "-"
	def __str__(self):
		return self.v
	def __init__(self,v1):
		print "creating " + v1
		self.v = v1	
	c = ()
	def add(self,e):
		print "adding " + str(e) + " to " + str(self)
		self.c = self.c + (e,)
	def children(self):
		return self.c

def preorder(n):
	print n,
	for e in n.children():
		preorder(e)
	print '#',
def serS(n):
	if n is None:
		return None
	s = str(n)
	for e in n.children():
		r = serS(e)
		if r is None:
			break;
		s = s + r
	s+= '#'
	return s
def mt(dq):
	print dq
	if ( (dq == None)  or (len(dq) == 0) ):
		return None
	c = dq.popleft();
	if (c == '#'):
		return None
	n = N(c)
	while True:
		ch = mt(dq)
		print ch
		if (ch is None):
			break;
		n.add(ch)
	return n

def test(n):
	serialStr = serS(n)
	nDeserialized = mt(deque(serialStr))
	if serialStr != serS(nDeserialized):
		print "Fail"
		exit(-1)
	else:
		print "Succss"

a1 = N('A')
test(a1)

for (c1,c2) in zip(string.lowercase,string.uppercase):
	setattr(sys.modules[__name__], "n"+c1,N(c2))

test(na)
na.add(nb)
test(na)
nb.add(nd)
test(na)
nb.add(ne)
test(na)
na.add(nc)
test(na)
nc.add(nf)
test(na)
nc.add(ng)
test(na)
test(na)


