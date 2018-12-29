#sets are unordered lists of unique items
#dicitonaries without key value pairs, same as in JS
myset = set()
myset.add(1)
print(myset)
myset.add(2)
myset.add(2)
print(myset)
#can't add same element multiple times, good for getting unique values
mylist = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
newset = set(mylist)
print(newset)
#good for grabbing out the unique values