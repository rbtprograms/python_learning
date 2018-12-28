str = 'this is a string'
otherStr = "this is also a string"

print("hello")
print('hello 2')
print('hello \n 3')
print(len('hello there firnds'))
print(str[0])
print(str[-1])
print(str[:4])
print(str[4:])
print(str[9:18])
print(str[::])
print(str[::3])

#the olon is how you slice strings, two indeces. from the first to the second.
#if one of the indeces is missing, it will start at beginning or go to end
#a start and a stop
#there is a also a third parameter, which is step size. How many indeces you want to go per loop
#default is one

print(str[::-1])
#this will reverse your string, start at beginning, go to end, each loop should go backwards
# and python has negative indeces which is nice

#in python strings are immutable
#to make new strings out of old strings you must concatenate

x = 'Hello World '
print(x + 'it is beautiful')
x = x + ' ADDED '
print(x)
#you can multiply strings
print(x * 3)

testStr = 'Hello World'
#how to upper case
print(testStr.upper())
#how to lower
print(testStr.lower())
#how to split into list
#defaults to split on whitespace
#can pass an arguement of something to split on
print(testStr.split())

#formatting strings to inject values
print('This is a {}. And this is {} string.'.format('string', 'another'))
##you can put index positions in the curlys and it grab the word at that index in the format call
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
#you can also declare and use variables
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

#float formats
result = 100/77
              #first number is width, adds space in front of number
              #second number is how many decimals you want to go to
print('*RESULTS: {r:1.5f}**'.format(r=result))

#formatting with string literals
name = 'Bobby'
age = 28
#putting f infront of string lets you add variables
print(f'Hello {name} you are {age} years old.')