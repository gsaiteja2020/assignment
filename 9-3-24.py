# 1.Write a program which will find all such numbers which are divisible by 7 but are not a 
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be 
# printed in a comma-separated sequence on a single line.

'''
list=[item for item in range(2000,3201) if item%7==0 and item%5!=0]
print(list)
'''

# 2.With a given integral number n, write a program to generate a dictionary that contains (i, 
# i*i) such that is an integral number between 1 and n (both included). and then the program 
# should print the dictionary. Suppose the following input is supplied to the program: 8 Then, 
# the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
''' 
num=int(input("Enter the number"))
dictionary={i:i*i for i in range(1,num+1)}
print(dictionary)'''

# 3.Write a program which accepts a sequence of comma-separated numbers from console 
# and generate a list and a tuple which contains every number. Suppose the following input 
# is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', 
# '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
''' 
string=input("enter the number sperated by comma")
l=string.split(",")
print(l)
t=tuple(l)
print(t)
 '''

# 4.Write a program that accepts a comma separated sequence of words as input and prints 
# the words ina comma-separated sequence after sorting them alphabetically. Suppose the 
# following input is supplied to the program: without, hello, bag, world Then, the output 
# should be: bag,hello,without,world
'''
string=input("enter the words sperated by comma - ")
l=string.split(",")
l.sort()
print(l)
 '''
 
# 5.Write a program that accepts a sentence and calculate the number of letters and digits. 
# Suppose the following input is supplied to the program: hello world! 123 Then, the output 
# should be: LETTERS 10 DIGITS 3
'''
string = input("enter the string that includes numbers and alphabets - ")
letter=0
digits=0
for c in string:
    if c.isalpha():
        letter=letter+1
    elif c.isdigit():
        digits=digits+1

print("Letters - "+str(letter))
print("Digits - "+str(digits))
 '''

# 6.Write a program that accepts a sentence and calculate the number of upper case letters 
# and lower case letters. Suppose the following input is supplied to the program: Hello 
# world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
 
'''string = input("enter the string that includes upper and lower case - ")
upper=0
lower=0
for c in string:
    if c.isupper():
        upper=upper+1
    elif c.islower():
        lower=lower+1

print("Upper - "+str(upper))
print("Lower - "+str(lower))
'''

# 7.Write a program that computes the net amount of a bank account based a transaction 
# log from console input.The transaction log format is shown as following: D 100 W 200 D 
# means deposit while W means withdrawal. Suppose the following input is supplied to the
# program: D 300 D 300 W 200 D 100 Then, the output should be: 500
'''
net_amount = 0

while True:
    transaction = input("Enter transaction (as 'D amount' or 'W amount') or 'done' to finish: ")

    if transaction.lower() == "done":
        break

    
    transaction_type, amount = transaction.split()
    amount = int(amount)

    
    if transaction_type == "D":
        net_amount += amount
    elif transaction_type == "W":
        net_amount -= amount


print("Net Amount:", net_amount)'''
