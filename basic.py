#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = 100
if a >= 0:
	print(a)
else :
	print(-a)

print('I\'m ok.')
print("I'm \"ok.")

print(True and False)
print(5>3 and 3>1)

print(10/3)
print(9/3)
print(10//3)
print(9//3)

print(ord('A'))
print(ord('中'))

print(chr(66))
print(chr(25991))


print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# print('中文'.encode('ascii'))

s1 = 72
s2 = 85
r = (s2 - s1) * 100/s1
print('提高的成绩百分比 %.1f %%' % r)

### list列表的使用，相当于数组.可变的有序表

classMate = ['chenyuliang','bob','kkjss','asdasd']
print(classMate,len(classMate),classMate[-2])

classMate.append('ads')
print(classMate,len(classMate))
classMate.insert(1,'sdss')
print(classMate,len(classMate))

#pop 删除
classMate.pop()
classMate.pop(0)
print(classMate,len(classMate))



### tuple 元祖  不可变的有序列表  不变的含义：每个元素指向的地址永远不变

chenll = ('asda','bbbbb','dccccc')
print(chenll)
	

####条件判断

'''
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''

birth = input('birth :')

if int(birth) > 2000:
	print('00后')
else:
	print('00前')

###所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
print (list(range(20)))

sum = 0
for x in range(101):
	sum = sum + x
print(sum)


### 字典类型  查找和插入速度快，不会随数量增大。占用内存大 key必须是不可变的对象


###set 无序的无重复元素的集合，可以做数学意义上的交集和并集运算。

v1 = set(['1','1','3','4','2','5','3'])
print(v1)