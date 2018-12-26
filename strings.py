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