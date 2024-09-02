# list concatination and manipulation
l=[1,2,3,4,5,6]
l2=[7,8,9,0]

print(l+l2)

print(l*3)

# comparing 2 lists
x=["Apple","banana","cat"]
y=["apple","banana","cat"]

print(x<y) #because x is having "A"and y is having "a"

#membership checking
a=[2,3,4]
b=[1,2,3,4,5]
print(1 in b)
print(1 not in a)

#nested  lists
a=[2,3,4,y,b]
print(a)
print(b in a)

print(a[3][2]) #accessing nested list

x=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(x)):
    for k in range(len(x[i])):
        print(x[i][k],end=" ")
    print("")

# list comprehension

#s=[expression for i in range(10) condition]
l=[x for x in range(10)]
print(l)

l=[x*x for x in range(10) if x%2==0]
print(l)

n=eval(input("enter"))
print(n)
print(type(n))