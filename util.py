
import collections
import string
import sys
import plyj.parser
import plyj.model as m
from collections import defaultdict
import glob
import os

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

# return List<fieldType0,fieldType1,fieldName>
def getFields(fileName):
    fieldList = [];
    p = plyj.parser.Parser()
    tree = p.parse_file(fileName)
    for type_decl in tree.type_declarations:
        for field_decl in [decl for decl in type_decl.body if type(decl) is m.FieldDeclaration]:
            print(field_decl)
            for var_decl in field_decl.variable_declarators:
                type_name0 = ""
                type_name1 = ""
                if type(field_decl.type) is str:
                    type_name0 = field_decl.type
                else:
                    type_name0 = field_decl.type.name.value
                    if len(field_decl.type.type_arguments) > 0:
                        type_name1 = field_decl.type.type_arguments[0].name.value
                print(var_decl) 
                
                print('    ' + type_name0 + ' ' + type_name1 + ' ' + var_decl.variable.name)
                fieldList.append((type_name0,type_name1,var_decl.variable.name))
    return fieldList;
def todo1():
	N = collections.namedtuple('N','v,children')

	for (c1,c2) in zip(string.lowercase,string.uppercase):
		setattr(sys.modules[__name__], "n"+c1,N(c2))

	na[children]  = (nb,nc);

	

