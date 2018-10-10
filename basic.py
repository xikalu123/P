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
