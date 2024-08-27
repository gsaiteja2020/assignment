#                                       STRING
# declaration
sin="satya"
sin1="satya123"
sin2="12345"

# accessing string
s="learn python"
print(s[-1])

print(s[1:6])

# s[startIndex:lastIndex:step]

print(s[0:12:2])


# STRING MANIPULATION

 # concatination
 
s1="python"
s2="django"

print(s1+" "+s2)

 # repetation

print((s1+" ")*10)

# STRING METHODS

 # find()   rfind()

word="learning python is easy"
print(word.find("y"))

print(word.find("arn"))

print(word.rfind("y"))

 # index()  rindex()

print(word.index("y"))

print(word.rindex("y"))


 # difference between find() and index() 


#  print(word.index("z"))  // gives error
print(word.find("z"))  #gives -1 as output whish resebles that the element is not present in the string

 # count()
word="python python python python python python python python python python python"
print(word.count("python"))


 # strip()
w= " learning "
print(len(w))
w1=w.strip()
print(len(w1))
# rstrip()
w= " learning "
print(len(w))
w1=w.rstrip()
print(len(w1))
# lstrip()
w= " learning "
print(len(w))
w1=w.lstrip()
print(len(w1))

 # split()
wd="where is the biryani from "
wdList=wd.split()
print(wdList)
wdList2=wd.split("e")
print(wdList2)
 