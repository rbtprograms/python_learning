#same defaults for functions
def name_of_function(name = 'NAME'):
  print(f'hello {name}')

name_of_function()
name_of_function('Bobby')

def add(a, b):
  return a + b
print(add(5, 9))

#finds house in provided string
def house_check(str):
  if 'house' in str.lower():
    return True
  else:
    return False

#better written like this
def dog_check(str):
  #since it already brings back a boolean
  return 'dog' in str.lower()

def pig_latin(word):
  first_letter = word[0]
  if first_letter in 'aeiou':
    return word + 'ay'
  else:
    pig_word = word[1:] + first_letter + 'ay'
  return pig_word