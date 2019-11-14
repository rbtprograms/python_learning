#lists hold marious objects, seperated by commas
#python also has arrays, and they do have differences
#can use multiple types, ordered list
myList = ['STRING', 100]
#len function to get length
print(len(myList))
#access indexs
myList[0]
#slice the same as strings
print(myList[:1])
#can concatenate by adding lists together
first = [1, 2]
second = [3, 4]
combined = first + second
print(combined)
#lists are mutable
combined[1] = 'TWO'
print(combined)
#append to add items to back
combined.append(66)
print(combined)
#pop to take them off, can be stored in variable
poppedItem = combined.pop()
print(combined)
print(poppedItem)
combined = second + first
#sort
combined.sort()
print(combined)
##None is the equivelent of javascript undefined
#reverse
combined.reverse()
print(combined)