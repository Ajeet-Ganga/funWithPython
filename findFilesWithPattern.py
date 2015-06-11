import os
from os.path import join, getsize
import re

strPattern = 'import(.*);\n(.*)\n(.*public class .*\n)'
strDirectory = './src'
re1 = re.compile(strPattern)
badFiles = set()
for root, dirs, files in os.walk(strDirectory):
	# print root,dirs,files
	for f in files:
		if '.java' in f:
			#print root,f
			with open(join(root,f)) as f1:
				for l in f1:
					if '@XmlRootElement' in l:
						# print l,f
						break
					if 'public' in l:
						if not 'enum' in l:
							badFiles.add(f)
print '-----------'
for f in badFiles:
	print f
