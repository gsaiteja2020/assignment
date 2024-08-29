#membership checking
# in and not in returns boolean value
s="learning python"
print("l" in s)
print("python" in s)
print("x" not in s)

# replace()

fname="pawan kalyan"
name=fname.replace("pawan","CM")
print(name)

# join()

s=["ram","shamyam","hari","ravi"]
l="-".join(s)
print(l) #ram-shamyam-hari-ravi

# endswith() startswith()

mail="gsaiteja2020@gmail.com"
website="https://skywavessoftware.com"

print(mail.endswith("@gmail.com"))
print(website.startswith("https://"))

# changing case of a string

# upper()
s="Learning python"
print(s.upper()) #LEARNING PYTHON
# lower
s="LEARNING PYTHON"
print(s.upper())#LEARNING PYTHON
# swapcase()
s="LearNinG pYtHon"
print(s.swapcase())#lEARnINg PyThON
# title
s="learning python"
print(s.title())#Learning Python
# capitalize
s="learning python"
print(s.capitalize())#Learning python

# how to check type of a character present ina string
#isalnum()
n="1223"
print(n.isalnum())
# isalpha()
c="asmamsks"
print(c.isalpha())
# isdigit()
d="1234"
print(d.isdigit())
# isupper()
char="A"
print(char.isupper())
# islower()
char="a"
print(char.islower())
# istitle()
char="Len Ten Lin"
print(char.istitle())
# isspace()
space="  "
print(space.isspace())




# ----------------------------------------------------------------------------------------------------------------------


            # Python Program to count occurrence of a given characters in string.

'''txt="concurence"
count=txt.count("c")
print(count)'''

            # Python Program to check if two Strings are Anagram.

'''s1 ="listen"
s2 ="silent"
if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.") 
else:
        print("The strings aren't anagrams.") '''

            # Python program to check a String is palindrome or not.

'''txt="madam"
txt2=txt[::-1]
if (txt == txt2):
   print("string is a palindrome")
else:
   print("string is not a palindrome")'''


            # Python program to replace the string space with a given character using replace() method.

'''string = "Hello World"
new_string = string.replace("Hello", "Good Bye")

print(new_string)'''

            # Python program to convert lowercase char to uppercase of string.

'''string = "hello world"
newString=string.upper();
print(newString)'''

            # Python program to convert lowercase vowel to uppercase in string.

'''str = "eutopia"
N = len(str)
     
str1 =""
     
for i in range(N):
        if (str[i] == 'a' or str[i] == 'e' or
            str[i] == 'i' or str[i] == 'o' or
            str[i] == 'u'):
            c = (str[i]).upper()
            str1 += c
        else:
            str1 += str[i]
 
print(str1)'''

            # Python program to separate characters in a given string.

'''str = "eutopia"
N = len(str)    

for i in range(N-1):
    
    print(str[i])
'''

            # Python program to remove blank space from string.


'''text = "Hello World, How Are You?"
text_no_spaces = text.replace(" ", "")

print("Original String:", text)
print("String without spaces:", text_no_spaces)'''

            # Python program to concatenate two strings using join() method.

'''var1 = "good"
var2 = "morning"

var3 = " ".join([var1, var2])

print(var3)'''

            # Python program to concatenate two strings without using join() method.

'''var1 = "good "
var2 = "morning"

var3 = var1 + var2
print(var3)'''

            # Python program to remove repeated character from string.



'''string = "succession"
p = ""
for char in string:
    if char not in p:
        p = p+char
print(p)'''

            # Python program to check given character is vowel or consonant.
'''x=input("enter the character ")
if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'): 
        print("Vowel") 
else: 
        print("Consonant")'''

            # Python program to check given character is digit or not.
'''
ch = input("Enter Character ")

if(ch >= '0' and ch <= '9'):
    print("The Given Character is a Digit")
else:
    print("The Given Character is Not a Digit")'''

            # Python program to delete vowels in a given string.

'''s = "perpituation"
result = ""

for i in range(len(s)):
    x=s[i]
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        pass
    else:
        result = result + s[i]

print("\nAfter removing Vowels: ", result)'''

            # Python program to count the Occurrence Of Vowels & Consonants in a String.

'''string = "Python Programming"
vowels = 'aeiouAEIOU'

vowel_count = 0
consonant_count = 0

for char in string:
    if char in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print(vowel_count)
print(consonant_count)'''

            # Python program to print the highest frequency character in a String.

'''string = "hello world"
max_count = 0
max_char = ''
    

for i in range(len(string)):
        count = 0
        
      
        for j in range(len(string)):
            if string[i] == string[j]:
                count += 1
        
        
        if count > max_count:
            max_count = count
            max_char = string[i]
    
print("max frecuency character is "+ str(max_char) + " with a count of "+str( max_count))'''


            # Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.

'''string = "hello world"
vowels = "aeiouAEIOU"

for i in range(len(string)):
    if string[i] in vowels:
        
        string = string[:i] + '-' + string[i+1:]
        break

print(string)'''


            # Python program to count alphabets, digits and special characters.

'''string = "Helloworld1232433!@#=&^%"


alphabets = 0
digits = 0
special_chars = 0


for char in string:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1


print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special characters:", special_chars)'''


            # Python program to check given character is digit or not using isdigit() method.

'''char = input("Enter a character: ")


if '0' <= char <= '9':
    print(f"'{char}' is a digit.")
else:
    print(f"'{char}' is not a digit.")'''

            # Python program to calculate sum of integers in string.
'''s= "a1er2e3e6df8fd4df6"
sum=0
for i in s:
    if i.isnumeric():
        sum+=int(i)
print(sum)'''

            # Python program to print all non repeating character in string.


'''s = "swiss"

char_count = {}

for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char in s:
    if char_count[char] == 1:
        print(char, end=' ')
            '''
            # Python program to copy one string to another string.


'''original_string = "Hello, World!"

copied_string = ''.join(original_string)

print("Original string:", original_string)
print("Copied string:", copied_string)'''

            