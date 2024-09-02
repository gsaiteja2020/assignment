#                                                      tuple
# it is collection of objects separated by comma
# similar to list. i has indexing, nested objects and repetation on common
# it is a immutable datatype, which means can't manipulate the data


# declaration and initialization
t=(1,2,3,4)
print(type(t))
t1=(1,) #if we dont add comma then it will be integer
print(type(t1))

# accesing elements from the tuple
tpl=(1,2,3,4,5,6,7,8,9)
print(tpl[5])

# different operations on tuple
t1=(1,2,3,4)
t2=("a","b","c","d")
# concatination
print(t1+t2)
# repetation
print(t1*2)


# nested tuple
t3=(1,2,3,4,t1,t2)
print(t3)
print(t3[4][2])

# slicing 
print(t3[1:7])

# usinig typecasting to alter data in tuple
mytuple=("python","java","javascript")
list=list(mytuple)
print(list)
list.append("html")
print(list)
mytuple=tuple(list)
print(mytuple)


# collectionn of multiple datatypes
t=("data",1,23.32,True,(1,2,3),["hello","woreld"])
print(t)

for n in t:
    print(n)


print(t.count(1))
print(t.index(1))

# ------------------------------------------ Assignment -----------------------------------------------------

# How do you create a empty tuple on python ?

'''emptyTpl = ()'''

# Write a python program to unpack atuple into several variables ?


'''t = (10, 20, 30)
a, b, c = t

print(a)  
print(b)  
print(c) ''' 


# write a python program to add an item to the tuple ? 

'''t = (1, 2, 3)
l = list(t)
l.append(4)
t = tuple(l)
print(t) '''


# Write a python proram to convert tuple into a string ?

'''t = ('hello', 'world')
string = ''.join(t)

print(string) 
'''

# Write a python program to find most frequent element in tuple ?

'''t = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
most_frequent_element = None
max_count = 0

for item in t:
    
    current_count = 0
    for element in t:
        if element == item:
            current_count += 1

    
    if current_count > max_count:
        max_count = current_count
        most_frequent_element = item

print(most_frequent_element) ''' 
