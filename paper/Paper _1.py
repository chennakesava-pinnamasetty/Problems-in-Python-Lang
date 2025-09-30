
# 1. Find the even & Odd numbers


'''
while True:                               # This creates an infinite loop (it keeps running forever).
 num = int(input("Enter a number :"))     # The program waits for the user to type a number.
 if  num == -1:                           # his checks if the user typed -1. If yes, then break stops the loop → program ends.
  break                                   # The only way out is if we use break.

 if num % 2 == 0:                      # If the number is not -1, the program checks num % 2 == 0.
       print("Even")                     # If true → prints Even.
 else:
       print("Odd" )                     # Otherwise → prints Odd.
     
'''
    # Loop goes back up

# After printing, the loop restarts at while True: and asks for another number.




# 2.  how to swap two variables 

     # The first one is a traditional method using the variable 'temp'.
     # The second one, on the other hand, can be done to save time.


# Traditional way

'''
a = 4
b = 7
c = 9

temp = a
a = b
b = c
c = temp

print('a = ',a)
print('b =', b)
print('c =', c)


# one hand

a = 3
b = 8
c = 7

a, b = b,a
print("A =",a)
print("b =",b)
print("c =",c)
'''


# 3. How to check if a number is prime number or not?
'''
num = int(input("Enter a Number :"))

for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
    '''


# (Conitinues loop )
'''
while True:
    num = int(input("Enter a number :"))

    if num == -1:
      break
       
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
      print("Prime")
      '''



# 4. How find out the factorial of a number?
'''
num = int(input("Enter a number :"))

fact = 1
for i in range(1, num + 1):
    fact *= i

print("Factorial of",num,"is",fact)

'''
    # Check if the number is negative, positive or zero

'''
while True:
 num = int(input("Enter a number :"))
 if num == -1:
  break
 
 fact = 1
 if num < 0:
     print("sorry, factorial does not exist for negative numbers")
 elif num == 0:
     print("The factorial 0 is 1")
 else:
     for i in range(1, num+1):
         fact *= i
     print("Factorial of",num,"is",fact)
     '''




# 5. How to generate random number in python


# 1. random float
    # Gives a random float number between 0 and 1 :
'''
import random
num = random.random()
print(f"{num:.2f}")
'''


'''
import random
num = random.uniform(1,100)
print(f"{num:.2f}")

'''


# 2 random integer
   # Gives a random integer in specified range:
'''
import random
num = random.randint(1,100)
print(num)
'''


# 3. random even number

     # Gives a random number in a range with incremental steps:
'''
import random
num = random.randrange(0,100,2)
print(num)
'''



# Random Series
    # Gives a series of random numbers

'''
import random

num = random.sample(range(0,100) ,3)
print(num)
'''




# 6. Print the first ten numbers of Fibonacci series in python

  # It is not just a great way to explore recursion and iterative techniques in programming.


# Iterative

'''
n = int(input("Entera how many terms you want :"))

a,b = 0,1
if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print(a)
else:
    print("Fibonacci series :")

    for _ in range(n):
        print(a, end=" ")
        a,b=b,a+b

'''

# Recursion

'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter how many terms you want :"))

print("Fibonacci series: ")

for i in range(n):
    print(fibonacci(i),end=" ")

    '''


def print_fibonacci(num):
    a,b = 0,1
    if num < 1:
        print("null")
    elif num == 1:
        print(a)
    elif num == 2:
        print(a)
        print(b)
    elif num >= 2:
        print(a)
        print(b)

        # genetate next num in the series
        for _ in range(num - 2):
            c = a + b
            # Update a and b to prepare for next iteration
            a,b = b,c
            # print the next term in the series
            print(c)

print_fibonacci(int(input("Enter a number : ")))