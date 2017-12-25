#-*-coding:utf-8-*-


import os
text = open("test.txt")

curPath = os.path.realpath(__file__)
curDir = os.path.dirname(curPath)
print curDir


txtfile = curDir+"\\test.txt"
print txtfile
'''
f = open(txtfile)
#print "%r \n" %f
#print f.read()

print f.readline();
print f.readline();
print f.readline();

f.close()
'''
f = open(txtfile,"a+")
f.write('1111\n')
f.write('2222\n')
f.write('3333\n')
f.close()
#print f.readline();
