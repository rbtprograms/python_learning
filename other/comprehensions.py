#list comprehensions are good ways to build lists easily

#super common way to build a list
mystring = 'hello'
mylist = []
for letter in mystring:
  mylist.append(letter)

#this saves programmer time but not computational time
#essentially you put things inide the empty list and let it build itself

mylist = [letter for letter in mystring]
#the first letter is what will be in the list, and the second is the actually for loop variable

mylist = [num for num in range(0, 20)]
#build a list with numbers in this range

mylist = [num**2 for num in range(0, 20)]
#build a list with their squares

#can use if statements
mylist = [x for x in range(0, 20) if x%2 == 0]

celcius = [0, 10, 20 ,34.5]

#essentially, the order is thing you want loop to do, loop logic, and else statements
#you can put elif statements in list comprehensions HOWEVER they are impossible to read
farenheit = [((9/5)*temp +32) for temp in celcius]
#gives temps in farenheit from the celcius list
#the same thing as below

fahrenheit = []
for temp in celcius:
  fahrenheit.append(((9/5)*temp + 32))

mylist = [x*y for x in [2,4,6] for y in [3,5,7]]