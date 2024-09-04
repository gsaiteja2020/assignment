# ====================================== SET ========================================

# to store multiple value in a single variable
# unordered
# immutable
# dublicates not allowed

s={"hello","khello","willow"}
print(s)

s={}
print(type(s)) # gives the type as dictionary

s=set()
print(type(s)) # now it gives the type as set




l=[1,1,2,3,3,4,2,2,4,5,6,6,7,7]
l=list(set(l))
print(l)

# adding new elements into sets
# add()
s1=set()
s1.add(20)
s1.add(30)
print(s1)
# update()
s2={1,2,3,4,5}
s1.update(s2)
print(s1)

# removing elements from set
# remove() >>  if we try to remove z from here it will give an error
names={1,2,3,4,5,6,7,8,9,0,"a"}
names.remove("a")
print(names)
# discard() >> if we try to remove z from here it will not give an error
names={1,2,3,4,5,6,7,8,9,0,"a"}
names.discard("z")
print(names)
# pop() >> removes element from random position
names={1,2,3,4,5,6,7,8,9,0,"a"}
names.pop()
print(names)

# clear() >> removes all elements from set
names.clear()
print(names)


# mathematical operations
# union >> returns a new set with element in both sets
s1={1,2,3,4,5,6}
s2={"a","b","c","d"}
print(s1.union(s2))
print(s1|s2)
# intersetion
s1={1,2,3,4,5,6}
s2={"a","b","c","d",1,2,3}
print(s1.intersection(s2))
print(s1&s2)
# differance >> returns the elements from 1st set but removes the common elements from 2 sets 
s1={1,2,3,4,5,6}
s2={"a","b","c","d",1,2,3}
print(s1.difference(s2))
print(s1-s2)
# symmetric-difference>> returns the uncommon elements
s1={1,2,3,4,5,6}
s2={"a","b","c","d",1,2,3}
print(s1.symmetric_difference(s2))
print(s1^s2)

se={1,2,3,4,5,6,7,8,3,42}
se.pop()
print(se)