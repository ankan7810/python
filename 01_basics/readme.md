# Object Types / Data Types

-Data type are in memory not in variable.
- Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True, False
- None : None
- Funtions, modules, classes

- Advance: Decorators, Generators, Iterators, MetaProgramming

SLICING:(in case of slicing we make copy of things)
>>> h1=[1,2,3]
>>> h2=h1[:]
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1[0]=55
>>> h1
[55, 2, 3]
>>> h2
[1, 2, 3]

COPY:
>>> import copy
>>> h2=copy.copy(h1)
>>> h2
[55, 2, 3]

CHECKING:
>>> h2==h1
True
>>> h2 is h1
False

CONCEPT 1: (at first listone,listtwo get same reference.after both are getting different reference.)
>>> listone=[1,2,3]
>>> listtwo=listone
>>> listone='chai'
>>> listtwo
[1, 2, 3]
>>> listone=[1,2,3]
>>> listone[0]=33
>>> listone
[33, 2, 3]
>>> listtwo
[1, 2, 3]

CONCEPT 2: ((l1,l2) get same only one reference here.which is l1's reference.)
>>> l1=[1, 2, 3]
>>> l2=l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0]=44
>>> l1
[44, 2, 3]
>>> l2
[44, 2, 3]

PRINTING TYPE: 
>>> repr('chai')
"'chai'"
>>> str('chai')
'chai'
>>> print('chai')
chai

BOOLEAN:
>>> 1 ==2 <3
False
>>> 1==2 and 2<3

MATH LIBARY:
>>> import math
>>> math.floor(3.5)
3
>>> math.floor(-3.5) 
-4
>>> math.floor(3.9)  
3
>>> math.trunc(2.8)
2
>>> math.trunc(-2.8) 

OCTAL:
>>> 0o45
37
>>> 0o20
16

HEXAL:
>>> 0xFF
255
>>> 0xcc
204
>>> 0x66
102

DECIMAL TO OCTAL:
>>> int('64',8)
52
DECIMAL TO HEXAL:
>>> int('64',16) 
100

DECIMAL ADDITION:
from decimal import Decimal 
>>> Decimal('0.1') +Decimal('0.1')+ Decimal('0.1') - Decimal('0.3') 
Decimal('0.0')

TRUE OR FALSE:
>>> True ==1
True
>>> False==0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> False is 0
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> True+4
5

SET OPERATION:
>>> setone={1,2,3,4,5}
>>> setone & {3,4}
{3, 4}
>>> setone | {3,4} 
{1, 2, 3, 4, 5}
>>> setone | {3,4,6} 
{1, 2, 3, 4, 5, 6}
>>> setone - {1,2,3,4,5} 
set()

STRING:
>>> chai ="Lemon Chai"
>>> chai
'Lemon Chai'
>>> print(chai.replace("Lemon","Ginger"))
Ginger Chai
>>> name="Ankan Roy"
>>> name
'Ankan Roy'
>>> chai ="Masala chai"
>>> print(chai.find("chai"))
7
>>> chai="Lemon,ginger,Masala,Mint"
>>> print(chai.split())
['Lemon,ginger,Masala,Mint']
>>> print(chai.split(", ")) 
['Lemon,ginger,Masala,Mint']
>>> print(chai.replace("Masala","Lemon"))
Lemon,ginger,Lemon,Mint
>>> chai ="Masala chai chai " 
>>> print(chai.count("chai"))
2
>>> quentity=2
>>> chai_type="Masala chai" 
>>> order="I orderred {} cups of {} " 
>>> order
'I orderred {} cups of {} '
>>> print(order.format(quentity,chai_type))
I orderred 2 cups of Masala chai
>>> chai ="Lemon Chai"
>>> chai
'Lemon Chai'
>>> print(chai.replace("Lemon","Ginger"))
Ginger Chai
>>> chai_varity=["Lemon","Ginger","Masala"]
>>> print("".join(chai_varity))
LemonGingerMasala
>>> print(" ".join(chai_varity)) 
Lemon Ginger Masala
>>> print("- ".join(chai_varity)) 
Lemon- Ginger- Masala
>>> print("=".join(chai_varity))  
Lemon=Ginger=Masala
>>> chai ="masala\nchai"
>>> chai
'masala\nchai'
>>> print(chai) 
masala
chai
>>> chai =r"masala\nchai" 
>>> print(chai) 
masala\nchai

REPLACE:
>>> chai_varity[1:2]=["Green"]
>>> chai_varity
['Lemon', 'Green', 'Masala']
>>> chai_varity=["Lemon","Ginger","Masala","Ginger"] 
>>> chai_varity[1:3]=["Green","Black"] 
>>> chai_varity
['Lemon', 'Green', 'Black', 'Ginger']

LOOPS:
>>> chai_varity=["Lemon","Ginger","Masala","Ginger","white"]
>>> for tea in chai_varity:
...     print(chai_varity)
...
['Lemon', 'Ginger', 'Masala', 'Ginger', 'white']
['Lemon', 'Ginger', 'Masala', 'Ginger', 'white']
['Lemon', 'Ginger', 'Masala', 'Ginger', 'white']
['Lemon', 'Ginger', 'Masala', 'Ginger', 'white']
['Lemon', 'Ginger', 'Masala', 'Ginger', 'white']
>>> for tea in chai_varity:
...     print(tea,end="-") 
...
Lemon-Ginger-Masala-Ginger-white->>>
>>> chai_varity
['Lemon', 'Ginger', 'Masala', 'Ginger', 'white']
>>> range(10)
range(0, 10)
>>> squared_nums=[x**2 for x in range(10)]
>>> print(squared_nums)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

DICTIONARY:
>>> chai_types={"Masala":"spicy","Ginger":"zesty","Green":"Mild"}
>>> chai_types
{'Masala': 'spicy', 'Ginger': 'zesty', 'Green': 'Mild'}
>>> chai_types["Masala"]
'spicy'
>>> chai_types.get("Masala")
'spicy'
>>> for chai in chai_types:
...     print(chai)
... 
Masala
Ginger
Green
>>> for chai in chai_types:
...     print(chai,chai_types[chai])
... 
Masala spicy
Ginger zesty
Green Mild
>>> for key,values in chai_types.items(): 
...     print(key,values)
...
Masala spicy
Ginger zesty
Green Mild
>>> if "Masala" in chai_types:
...     print("I have masala chai")
...
I have masala chai
>>> print(len(chai_types))
3
>>> chai_types["Black chai"]="sexy"
>>> chia_types
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'chia_types' is not defined. Did you mean: 'chai_types'?
>>> chai_types
{'Masala': 'spicy', 'Ginger': 'zesty', 'Green': 'Mild', 'Black chai': 'sexy'}
>>> chai_types.pop("Ginger")
'zesty'
>>> chai_types
{'Masala': 'spicy', 'Green': 'Mild', 'Black chai': 'sexy'}
>>> chai_types.popitem()
('Black chai', 'sexy')
>>> chai_types
{'Masala': 'spicy', 'Green': 'Mild'}
>>> del chai_types["Green"]
>>>
>>> chai_types
{'Masala': 'spicy'}
>>> chai_types_copy=chai_types.copy() 
>>> tea_shop={
... "chai":{"Masala":"spicy","Ginger":"zesty","Green":"Mild"},
... "Tea":{"Black chai":"sexy","white chai":"Good"}
... }
>>>    
>>> tea_shop
{'chai': {'Masala': 'spicy', 'Ginger': 'zesty', 'Green': 'Mild'}, 'Tea': {'Black chai': 'sexy', 'white chai': 'Good'}}
>>> tea_shop["chai"] 
{'Masala': 'spicy', 'Ginger': 'zesty', 'Green': 'Mild'}
>>> tea_shop["chai"]["Ginger"]
'zesty'
>>> squred_num={x:x**2 for x in range(6)}
>>> squred_num 
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squred_num.clear()
>>> squred_num
{}
>>> keys=["Masala","Ginger","Lemon"]
>>> default_value="Delicious"
>>> new_dict=dict.fromkeys(keys,default_value)  
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict=dict.fromkeys(keys,keys)            
>>> new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}

LIST:
>>> tea_types[0]
'Black'
>>> tea_types[-1] 
'oolong'
>>> tea_types[1:]
('Green', 'oolong')
>>> tea_types[0]="Lemon"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> len(tea_types)
3
>>> more_tea=("Herbal","Earl Grey")
>>> all_tea=more_tea+tea_types 
>>> all_tea 
('Herbal', 'Earl Grey', 'Black', 'Green', 'oolong')
>>> if "Green" in all_tea:
...     print("I have green tea")
...
I have green tea
>>> more_tea=("Herbal","Earl Grey","Herbal") 
>>> more_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> tea_types=("Black","Green","oolong")
>>> tea_types                           
('Black', 'Green', 'oolong')
>>> (black,green,oolong)=tea_types
>>> black
'Black'