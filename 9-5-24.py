# ================================ Dictionary ===============================
d= {}
print(type(d))

d=dict()
print(type(d))

# adding elements into dictionary
d["name"]="ram"
d["id"]=1001
d["salary"]=30000
print(d)

# printing particular element
print(d["id"])
print(d["name"])

# updating values
d["salary"]=40000
print(d)

# deleting elements
del d["id"]
print(d)


# FUNCTIONS
# len()
print(len(d))
# get() >> used to retrive data from dictionary
print(d.get("name"))
# pop() >> used to remove the element using key and returns only the value
print(d.pop("salary"))
print(d)
# popitem() >> removes key and value in form of tuple
print(type(d.popitem()))
# keys() >> returns only the keys
d={'name':'ram','id':1001,'salary':30000}
print(d.keys())
# values() >> returns only the values
d={'name':'ram','id':1001,'salary':30000}
print(d.values())
# items() >> returns both key and value as tuple
print(d.items())
# update() >> adds new key and value
x={'company':'tcs'}
d.update(x)
print(d)

# taking key and value from user
'''dict={}
for k in range(3):
    key=input("enter you key : ")
    value=input("enter you value : ")
    dict[key]=value
print(dict)'''

# -------------------------------------------------------ASSIGNMENT----------------------------------------------------------
# Write a python program to  add a key to a dictionary ?

'''d={}
key=input("enter the key : ")
value=input("enter the value : ")
d[key]=value
print(d)'''

# Write a python program to check weather the given value is present in the dictionary or not ?

'''dict = {
    'name': 'sai',
    'age': '25',
    'city': 'delhi'
}

to_check = input("enter the value you want to check : ")

if to_check in dict.values():
    print(f"The value '{to_check}' is present in the dictionary.")
else:
    print(f"The value '{to_check}' is not present in the dictionary.")'''

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values
#  are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

'''dict={key:key*key for key in range(1,16) }
print(dict)'''

# Write a python program to create a dictionary from the string ?

'''
string = input("Enter a string : ")
dict = {char: string.count(char) for char in string}
print(dict)'''

# Write a python program to combine two dictionaries by adding values of common keys ?

'''
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 35}
 

for key, value in dict2.items():
    if key in dict1:
        dict1[key] += value  
    else:
        dict1[key] = value  

print(dict1)'''

# Write a python program to merge two python dictionaries ?
'''
dict1 = {'a': 1, 'b': 2, 'c':8}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)'''

# Write  a python program to sort dictionary by keys or values ?

'''
dict45 = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
sorted_by_keys = dict(sorted(dict45.items()))
print("Dictionary sorted by keys:", sorted_by_keys)
'''

# Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

'''
string = input("Enter a string : ")
dict = {char: string.count(char) for char in string}
print(dict)'''