mylist = [1,2,3]
#range is useful to get standard items
#prints all 10
for num in range(10):
  print(num)

#prints 3-10
#start value, end value
for num in range(3, 10):
  print(num)

#step by 2
for num in range(0, 10, 2):
  print(num)

#how to build a list out of it
list(range(0, 11, 2))

#enumerate function
#having an index counter is, naturally, very common so we can access those values at that index
index_count = 0
word = 'abcdefg'
for letter in word:
  print(word[index_count])
  index_count += 1

#do this instead
#enumerate gives back tuples with the value and its index
word = 'abcdefg'
for letter in enumerate(word):
  print(letter)

for index, letter in enumerate(word):
  print(f'letter is {letter} at {index} index')

#zip function
#inverse enumerate
first = [1,2,3]
second = ['a', 'b', 'c']
# this just gives a mem location for where your zipped item is
zip(first, second)

#this returns tuples, with first in the first position and second in the second
#this is why tuple unpacking is so important
for item in zip(first, second):
  print(item)

#works with 3 items as well
third = [100, 200, 300]
for item in zip(first, second, third):
  print(item)

#if you zip different length items, it wont throw but it will only zip up to the shortest length, dropping other thigns off

#in operator
'x' in [1,2,3]
#False
1 in [1,2,3]
#True
#easy way to see whats in something
'mykey' in {'mykey':345}
#True
d = {'mykey':345}
345 in d.values()
#True

#min and max
newlist = [1, 100]
print(min(newlist))
#1
print(max(newlist))
#100

#random library
#python has a lot of built in libraries

from random import shuffle
newlist = [1,2,3,4,5,6,7,8,9]
shuffle(newlist)
print(newlist)

#shuffle does not return a new list
random_list = shuffle(newlist)
#the above item is nothing

from random import randint
randint(2, 199)
#this does return a value so you can save it

mynum = randint(0, 10)
#above holds an item

#input creates an input that users can put stuff into
result = input('what is your name?')
#will store whatever user put in in the variable
#will always be a string
