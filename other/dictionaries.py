#key value pairs
#unordered, cant be sorted
my_dict = {'key1': 'value1', 'key2': 'value2'}
#keys should be strings
print(my_dict['key1'])
#dictionaries use bracket notation for lookups, not dot notation
#can hold lists, dictionaries, numbers, strings
my_dict['key3'] = {'super_key': 1000}
print(my_dict['key3']['super_key'])
#dictionary methods
#all of these return lists
#grab the keys
print(my_dict.keys())
#grab the values
print(my_dict.values())
#grab the items converted to tuples
print(my_dict.items())