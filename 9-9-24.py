# ==================================== FUNCTION =========================================
def getEven(l):
    l1=[]
    for i in l:
        if(i%2==0):
            l1.append(i)
    print(l1)

l1=[1,2,3,4,5,6,7,8,9]
getEven(l1)

def wish(name):
    print("Happy Birthday",name)

wish("ram")
wish("krishna")

# types of arguments
'''
1.positional arguments >>> takes in positional order

2.keyword arguments >>> actual arguments are assigned to variable , it wont take in order of position rather
   takes the value assigned to variable

3.default arguments >>> we can assigen default value to function arguments ,
   when ever we dont pass that value while calling the method , the default value will be concidered

4.variable length arguments >>> multiple variale can be assigned to one argument in function by adding * to it. Ex- *n

5.keyword variable length arguments >>> multiple keyword arguments arr passed in the form of dictionary. Ex- **n
'''
# 1.positional arguments 
def calculation(x,y):
    print(x-y)

calculation(10,20)


# 2.keyword arguments 
def calculation(x,y):
    print(x-y)

calculation(x=10,y=20)

def calculation(x,y):
    print(x-y)

calculation(y=20,x=10)


# 3.default arguments
 
def greet(name, msg="good morning"):
    print(name,msg)

greet("sai","good evening")
greet("hari")

# 4.variable length arguments 

def sum(*n):
    sum=0
    for i in n:
        sum+=i
    print(sum)

sum(10)
sum(1,2,3,4,5,6,78,8,9)

# 5.Keyword variable length arguments
def display(**n):
    for i,j in n.items():
        print(i,"-",j)

display(s1=10,s2=20,s3=30,s4=40)