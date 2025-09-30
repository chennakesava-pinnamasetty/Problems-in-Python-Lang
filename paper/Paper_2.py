

# 1. write a python function that will reverse a string without using Slicing operation or reverse() function

# Here used stack looping fuction:

def exchange(s):
    result = " "
    for char in s:
        result = char + result
    return result


text = "chenna"
print(exchange("text"))

         # or

print(exchange("Chenna"))



# 2. Reverse a string without using slicing or loops
  # we used Recursion

def exchange(s):
    if len(s) == 0:
        return s
    return exchange(s[1:]) + s[0]

text = "kesava"
print(exchange(text))


# Another method to reversing the string.
# Slicing

txt = " chennakesava"
print(txt[::-1])



# 3. Write a program to delete all consonants from a given string. "Python and Data Structure"


def Remove_const(s):
    vowels = "aeiouAEIOU"
    result = " "
    for char in s:
        if char in vowels or not char.isalpha():
            result += char
    return result
    
print(Remove_const("Python and Data Structure"))





# 4 Write a program that will find the sum of all the prime numbers between 1 and N

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

def Sum_of_primes(N):
    total = 0
    for num in range(2,N+1):
        if is_prime(num):
            total += num
    return total

N = 20
print("sum of primes between 1 and", N,"is :", Sum_of_primes(N))



