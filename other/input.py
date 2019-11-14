x = input("x: ")
print(int(x))
print(float(x))
print(bool(int(x)))

age = 22
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

if age < 40:
  print('Not middleage')
else:
  pass

name = 'Bob'

if not name.strip():
  print('name is empty')
else:
  pass

names = ['Bob', 'AJohn']

for name in names:
  if name.startswith('J'):
    print('fOUND')
    break
else:
  print('nothing found')