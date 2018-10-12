
import math
##函数调用
print(abs(-100))

print(int('123'),int(12.34),float('12.34'),str(100),bool(1),bool(''))

jueduizhi = abs

print(jueduizhi(-10))


###函数定义

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x


print(my_abs(-123))

#空函数

def nop():
	pass

def move(x,y,step,angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

x,y = move(100,100,6,math.pi/6)
print(x,y)

r = move(100,100,6,math.pi/6) #return a tuple
print(r)


###函数参数
# n=2 默认参数
def power(x,n=2):
	s = 1
	while n>0:
		n = n - 1
		s = s * x

	return s



print(power(5))
print(power(5,3))

##默认参数必须指向不可变的类型

##错误做法
def add_end(l = []):
	l.append('END')
	return l
add_end()
add_end()
print(add_end())

##正确做法
def add_end(l = None):
	if l is None:
		l = []
	l.append('END')
	return l
add_end()
add_end()
print(add_end())

#可变参数

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print(calc(1,2,3,4,5))

nums = [1,2,3,4,5]
nums1 = (1,2,2,3,4,5,5)
print(calc(*nums1))




