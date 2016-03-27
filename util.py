import collections
import string
import sys


################################################################################
##### Functions
################################################################################
def getFiles(dirName, fileEnd):
    print(dirName)
    fileNameList = []
    for root, dirs, files in os.walk(dirName):
        print(root, dirs, files);
        for file in files:
            if file.endswith(fileEnd):
                fileName = os.path.join(root, file)
                print(fileName)
                fileNameList.append(fileName)
    return fileNameList

def todo1:
	N = collections.namedtuple('N','v,children')

	for (c1,c2) in zip(string.lowercase,string.uppercase):
		setattr(sys.modules[__name__], "n"+c1,N(c2))

	na[children]  = (nb,nc);

	

