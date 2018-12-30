st = 'Print only the words that start with s in this sentence'
for word in st.split():
  if word[0] == 's' or word[0] == 'S':
    print(word)

for num in range(0, 11):
  if(num%2 == 0):
    print(num)

mylist = [num for num in range(1, 51) if num%3 == 0]

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
  if(len(word) % 2 == 0):
    print('even!')

for num in range(1, 101):
  if(num%15 == 0):
    print('Fizzbuzz')
    continue
  elif(num%5 == 0):
    print('Buzz')
  elif(num%3 == 0):
    print('Fizz')
  else:
    print(num)

st = 'Create a list of the first letters of every word in this string'
mylist = [word[0] for word in st.split()]