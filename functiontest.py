def myfunc(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def myfunc2(*numbers):
    res = []
    for number in numbers:
        if number % 2 == 0:
            res.append(number)
    return res

def myfunc3(string):
    res = ''
    for index, letter in enumerate(string):
        if index % 2 != 0:
            res += letter.upper()
        else:
            res += letter.lower()
    return res

print(myfunc3('anthropomorphism'))

