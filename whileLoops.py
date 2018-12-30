x = 0

while x < 5:
  print(f'the current value of x is {x}')
  x += 1

#can else off of while loops
else: print('x is not less than 5')

#break breaks out of the loop
#continue goes to the top of the closest enclosing loop
#pass does nothing

x = [1 , 2, 3]
for item in x:
  #will get syntax error if theres nothing, put pass so it doesn't throw
  pass

for item in x:
  if item == 2:
    continue
  print(item)