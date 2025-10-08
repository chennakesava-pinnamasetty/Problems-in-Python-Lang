

base = int(input("Enter a number :"))
exp = int(input("Entera exponent :"))

result = pow(base,exp)
print(f"{base} raised to the power {exp} is : {result}")


'''
Enter a number :2
Entera exponent :5
2 raised to the power 5 is : 32
'''


# 2

base = int(input("Enter a number :"))
exp = int(input("Entera exponent :"))

result = base ** exp
print(f"{base} raised to the power {exp} is : {result}")


'''
Enter a number :2
Entera exponent :5
2 raised to the power 5 is : 32
'''



# Loop

base = int(input("Enter a number :"))
exp = int(input("Entera exponent :"))

result = 1
for i in range(exp):
    result *= base
print(f"{base} raised to the power {exp} is : {result}")