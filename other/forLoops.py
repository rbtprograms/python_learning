# most objects in python are iterable
# you can iterate over keys in dictionaries
my_list = [1, 2, 3]
for item_name in my_list:
    print(item_name)

# some general for loop examples
# you know how these work Bobby good lord

# how to loop through values in a dictionary
my_iterable = {'key1': 1, 'key2': 2}
for key in my_iterable:
    print(my_iterable[key])

for num in my_list:
    if(num % 2 == 0):
        print(f'Even Number {num}')
    else:
        print(f'Odd number {num}')

for num in my_list:
    list_sum += num
print(list_sum)

# prints each letter in string cause strings are iterable
for letter in 'Bobby':
    print(letter)

# if you don't need to use the variable, it is common to use an underscore
for _ in my_list:
    print('cool')

# you can iterate through tuples
# loops are good for what is known as tuple unpacking
tup_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
# it is super common in python for things in python to be packaged this way
# pairs and sequences of tuples are always coming up
# the below is how you unpack tuples, with multiple variables in your for loops
for a, b in tup_list:
    print(a)
    print(b)

# another way to work with dictionaries
for item in my_iterable.items():
    print(item)
# the above returns a list of tuples so we can unpack it
for key, value in my_iterable.items():
    print(value)

for value in my_iterable.values():
    print(value)
# the above does the same thing
