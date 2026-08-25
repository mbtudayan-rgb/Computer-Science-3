#CODE 1
def greet_students (name, nChar):
    for i in range(nChar):
        print(name[i])

name = input("Enter a Name: ")
nChar = input("Enter any numeric number: ")
nChar = int(nChar)
greet_students (name, nChar)
#------------------------------------------------#
#A. OUTPUT: 
#   J        That is the output since range(nChar)
#   o        just generated 0 up to (but not
#   s        including) 5.
#   e       
#   p       

#B. OUTPUT:
#   J
#   o
#   s
#   e      
#   p       That is the output since "Joseph The Dreamer"       
#   h       is only 18 characters long. It can succesfully
#           print all 18 characters, but when i hits 18,
#   T       name[18] doesnt exist.
#   h
#   e
#   
#   D
#   r
#   e
#   a
#   m
#   e
#   r 
#   IndexError: string index out of range

#C. Ill modify the code by using try/except:
def greet_students (name, nChar):
    try: #modified
        for i in range(nChar):
            print(name[i])
    except IndexError: #modified
        print(" nChar exceeds the length of the name.") #modified

name = input("Enter a Name: ")
nChar = input("Enter any numeric number: ")
nChar = int(nChar)
greet_students (name, nChar)
#------------------------------------------------#

#CODE 2
def greet_students (name, nChar):
    for i in range(nChar)
        print(name[0: nChar])

name = input("Enter a Name")
greet_students (name, len(name))
#------------------------------------------------#
#A. ERROR:
#   for i in range(nChar)
#
#   FIXED:
#   for i in range(nChar):
#       in order to fix it, I just added a colon at the
#       end of the line.

#B. Inverted Triangle
def greet_students (name, nChar):
    for i in range(nChar):
        print(name[0: nChar - 1])

name = input("Enter a Name")
greet_students (name, len(name))
#------------------------------------------------#

#CODE 3
n = 0
while n < 1 or n > 100:
    n = input("Enter a Number from 1 to 100 : ")
    n = int(n)

print("Sum of all squared numbers is", sum_of_squared(n))
#------------------------------------------------#
#A. Function Needed
def sum_of_squared(n):
    total=0
    for i in range (1, n+1):
        total += i**2
    return total
#------------------------------------------------#