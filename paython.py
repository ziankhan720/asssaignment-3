Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # a tuple of string
>>> fruits_tuple = ('apple', 'banana', 'cherry')
>>> print(fruits_tuple[0])
apple
>>> print(fruits_tuple[1])
banana
>>> print(fruits_tuple[-1])
cherry
>>> print(fruits_tuple[-2])
banana
>>> tuple1=(1,2,3)
>>> tuple2=(4,5,6)
>>> combine_tuple=tuple1+tuple2
>>> print(fruits_tuple[-2])
banana
>>> tuple1 = ('hello',)
>>> repeated_tuple = tuple1 * 5
>>> print(repeated_tuple)
('hello', 'hello', 'hello', 'hello', 'hello')
>>> numbers = (0, 1, 2, 3, 4, 5, 6)
>>> print(numbers[1:4])
(1, 2, 3)
>>> print(numbers[:3])
(0, 1, 2)
>>> print(numbers[4:])
(4, 5, 6)
>>> fruits_tuple=('banana','apple','orange','cherry','banana')
>>> print(fruits_tuple.count('banana'))
2
>>> print(fruits_tuple.index('cherry'))
3
>>> 
