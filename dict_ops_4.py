#Dictionary Operations

my_dict = {"brand": "Ford","model": "Mustang","year": 1964}
my_dict2 = {"brand": "Honda","model": "Accord","year": 2015}

#Access Element
print(my_dict['brand'])
print(my_dict['model'])
print(my_dict['year'])

#Add element to dictionary
my_dict['HP'] = 450
print(my_dict)

#Access Keys
print(my_dict.keys())

#Access Values
print(my_dict.values())

#Delete elements
# del my_dict2
# print(my_dict2)

#Clears dictionary, but dictionary still exists
my_dict2.clear()
print(my_dict2)

#Pop, deletes specific key in dictionary
my_dict.pop('model')
print(my_dict)

#Popitem, deletes last added item
my_dict.popitem()
print(my_dict)

#Dictionary comprehension
a = {i: i **2 for i in (1,2,3,4)}
print(a)

#Merge 2 dictionaries
x = {'a' : 5, 'f': 6}
y = {'z' : 4, 'd': 9}

dict3 = x | y
print(dict3)

#Merge 2 dictionaries with item unpacking

dict3 = {**x,**y}
print(dict3)

#Append a dictionary to a list

dict1 = {'Peepo' : 33}
list1 = [1,2,3,69]

list1.append(dict1.copy())
print(list1)

c = [12,32,44,55,66]

print(c[-2:])
