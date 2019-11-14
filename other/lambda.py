def square(num):
    return num**2


nums = [1, 2, 3, 4]

print(map(square, nums))
for item in map(square, nums):
    print(item)
print(list(map(lambda num: num**2, nums)))


def splicer(string):
    if len(string) % 2 == 0:
        return 'EVEN'
    else:
        return string[0]

names = ['Andy', 'bobby', 'james']
print(list(map(splicer, names)))

def check_even(num):
  return num % 2 == 0

print(list(filter(check_even, nums)))
print(list(filter(lambda num: num % 2 != 0, nums)))
