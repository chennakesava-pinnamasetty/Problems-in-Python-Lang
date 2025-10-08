

n = int(input("Enter a number : "))
print("The fators are :")
for i in range(1,n+1):
    if n % i == 0:
        print(i,end=" ")


'''
Enter a number : 12
The fators are :
1 2 3 4 6 12
'''
print()




# Finding out the Prime Factors of a Number

'''
What are Prime Factors?

Prime factors are the prime numbers that divide a number exactly.

Example: Number = 12

Factors of 12 = 1, 2, 3, 4, 6, 12

Prime factors = 2, 3 (because 2 and 3 are prime numbers)
'''


n = int(input("Enter a number : "))

i = 2
print("Factors :")

while i <= n:
    if n % i == 0:
        print(i,end=" ")
        n = n//i
    else:
        i += 1 


'''
Enter a number : 12
Factors :
2 2 3
'''