# LAMBDA expression
# syntax---> lambda arguments : expression
# example 1
n=5
l= lambda x:x*x
print(int(l(n)))
# example 2
def find_big(a,b):
    if a>b:
        return a
    else:
        return b

print(find_big(10,20))

find=lambda a,b:a if a>b else b
print(find(10,20))

# filter()

# filter(function, sequence)
def getEvens(x):
    if x%2==0:
        return x
    
l=[1,2,3,4,5,6,7,8,9]
l1=filter(getEvens,l)
print(list(l1))

# MAP
# syntax-->map(function, sequence)
def sqr(x):
    return x*x

l=[1,2,3,4,5,6,7,8,9]
l1=map(sqr,l)
print(list(l1))

# ------------------------------------------ ASSIGNMENT ---------------------------------------------------
# lst=["1","2","3","4","5","6","7","8","9"]
# return the squares
lst=["1","2","3","4","5","6","7","8","9"]
sqrList=[]
for x in lst:
    ele= int(x)
    sqrList.append(ele*ele)

print(sqrList)

# s="learning python is easy"
# o/p - "easy is python learning"
# o/p - ""

s="learning python is very easy"
f1=s.split()[::-1]
s1=""
for x in f1:
    s1= s1+x+" "
print(s1)

s2=""
for x in f1:
    s2=s2+x[::-1]+" "
print(s2)