def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


# supports named parameters being passed
print(increment(2, by=3))
print(type(increment(2, 3)))
print(increment(6))

# how to do a variable amount of arguements


def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# automatically builds a dictionary out of arguements
def save_user(**user):
  print(user)

save_user(id=123, name='bobby')
