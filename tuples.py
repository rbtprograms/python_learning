#tuples are very similar to lists only one main difference
#THEY ARE IMMUTABLE
#they are not contained in brackets, they are in parens
tup = (1, 2, 3)
lis = [1, 2 ,3]
print(type(tup))
print(type(lis))
#can grab indexes
print(tup[1])
print(tup[2])
tup = (1, 2, 1, 1, 3)
#count items
print(tup.count(1))
#find index of first item
print(tup.index(2))
#tuples are immutable, you cant reassign items. This is main difference