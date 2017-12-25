#-*-coding:utf-8-*-
#from __future__ import division 擦这个不能用注释
from __future__ import division

#001
print "hello py"
print 'dasemimi'
print "d'a'se'm'imi"
print 'i "am" dasemimi'
print "dasemimi."
print "大色秘密"
print "dasemi#mi"

#002

print "大色你还有多少钱？ ",100-25*3%4

print "我我现在还有这么多 ",25+5/3

print 5<3,1>0

print 5/3


#myAge = 80 
#yourAge = 70
#可以写成这样
myAge,yourAge = 80 , 70
print "myAge - yourAge = " ,myAge - yourAge

#多行注释

'''
我是多行注释
你是多行注释
我们都是注释
'''

dogName  ,eggCount = 'xiaomi' ,100

print "MyDogName %s" %dogName
print "myEggCount %d" %eggCount
print "我家的狗的名字叫做 %s 我家有鹅蛋 %d 个" %(
	dogName,eggCount
	)


#'%d' %10


print 'aaa %r bbbb' %'dafsasdfasdf'
print "dase"+"mimi"
v1='dase'
v2='mimi'
print v1+v2

print ".a"*10

print "%r %r %r %r" %(True,False,0.02,round(3.1415926538))

print "\""


for i in {1,2,3,"3","4"}:
	print "%r"%i,

Mystr = '''
fsdfsadfs
'''
print Mystr

#print "请输入: "
#abc = raw_input()
#print abc

print int("10")
print u'35'

from sys import argv

for i in argv:
	print i,


