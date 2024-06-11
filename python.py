Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
abs(-10)
10
abs(34)
34
abs(-54)
54
>>> abs(3+3j)
4.242640687119285
>>> a=-20
>>> abs(a)
20
>>> a
-20
>>> a=abs(a)
>>> a
20
>>> ceil(45.4)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ceil(45.4)
NameError: name 'ceil' is not defined
>>> math.ceil(34.2)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    math.ceil(34.2)
NameError: name 'math' is not defined
>>> import math
>>> math.ceil(45.3)
46
>>> math.ceil(87.4)
88
>>> math.ceil(-43.5)
-43
>>> math.floor(67.4)
67
>>> math.floor(65.9)
65
>>> math.floor(45.5)
45
>>> math.floor(-56.2)
-57
>>> a=0.3
>>> math.floor(a)
0
