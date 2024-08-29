#                                                     LIST
l=["name",123,12.23,True]
print(l)

# how to create a list

l=[]#empty list

l1=list("python")
print(l1)

name="p y ton"
s1=name.split()
print(s1)

# accessing elements from list

l=[1,2,3,4,5,6,7,8,9,0]
print(l[0])

print(l[1:9:2])

print(l[-1])


# adding a new elememt into the list
l=[1,2,3,4,5,6,7,8,9,0]
l[9]=10
print(l)
# append()>> adds elements at the end of the list
l.append(20)
print(l)
# insert()>> adding element in a specified location
l.insert(10,"praveen")
print(l)


# adding one list with another list
l1=[1,2,3,4,5,6]
l2=[7,8,9,0]
# extend()
l1.extend(l2);
print(l1)
#use concatination +
l3=[1,2,3,4,5,6]
l4=[7,8,9,0]
print(l3+l4)


# iterating through list

for item in l:
    print(item)


# removing element from list
# pop()>> it removes last element. it follows LIFO
l=["name",12,23.32,True]
l.append(False)
print(l)
print(l.pop())
print(l)
# remove()>> removes specified element from the list
l.remove("name")
print(l)

# clear()>> remove all the elements
l.clear()
print(l)

# del >>delete the variable
del l
# print(l) >> l variable is not found


# aliasing and cloning of list
names=["ram","shiva","krishna","vishnu"]
n=names #this statement copies the elements but the address is same. so it is not recommended
print(id(names))#2538581963648
print(id(n))#2538581963648

n1=names.copy()
print(id(n1))#2400798472768
# cloning by using of slice operate
n2=names[:]
print(id(n2))#2466801299776


# ordering of list
#reverse()
names=["ram","shiva","krishna","vishnu"]
print(names)
names.reverse()
print(names)
# sorting
l=[1,2,3,4,5,6,7,8,934,667,21,00,456,32234,12,11,1,89]
l.sort()
print(l)










