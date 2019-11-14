x = 1
y = 1
unit_price = [1,2,3]
print(unit_price)
print(id(unit_price))
unit_price.append(4)
print(id(unit_price))

test = "hi"
test2 = "there"
print(len(test))
print(test[-1])

full = f"{test} {test2} {2+2}"
print(full)

sample = "    this Is a Test for stuFF"
print(sample.upper())
print(sample.lower())
print(sample.title())
print(sample.strip())
print(sample.find('T'))
print(sample.find('WOW'))
print('stuFF' in sample)
print('stuFF' not in sample)
print(sample.replace(' ', 'SPACE'))

# binary
print(0b10)
print(bin(10))
# hex
print(0x12c)
print(hex(50))

# complex number
z = 1 + 2j
print(z)


# no constants in pythons o use all camps
PI = 3.14
print(round(PI))
print(abs(-2))