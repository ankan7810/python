>>> f=open('chai.py')
>>> f.readline()
'import time\n'
>>> f.readline()
'\n'
>>> f.readline()
'print("hii")'
>>> f.readline()

RAW WAY:
>>> m=open('chai.py')
>>> m.__next__()
'import time\n'
>>> m.__next__()
'\n'
>>> m.__next__()
'print("hii")'
>>> m.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

>>> for line in open('chai.py'):
...     print(line)
...
import time



print("hii")

WHILE LOOP:
>>> m=open('chai.py')
>>> while True:
...     line=m.readline()
...     if not line:break
...     print(line,end='')
...
import time

print("hii")>>>

IF CASE:
>>> a='ankan'
>>> if not a:
...     print(a)
...
>>> a=''
>>> if not a:  
...     print('ankan')
...
ankan

ITERABLE LOOPS:
>>> mylist=[1,2,3,4]
>>> i=iter(mylist)
>>> i
<list_iterator object at 0x000001EE91A6F370>
>>> i.__next__()
1
>>> i.__next__()
2
>>> i.__next__()
3
>>> i.__next__()
4
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

ITERABLE FILE:
>>> f=open('chai.py')
>>> iter(f) is f      
True
>>> iter(f) is f.__next__()
False
>>> iter(f) is f.__iter__() 
True

ITERABLE DICT:
>>> D={'a':1,'b':2}
>>> for key in D:
...     print(key)
...
a
b
RANGE:
IT IS ITERABLE