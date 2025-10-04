
#

a = "chenna"

if a == a[::-1]:
    print(a,"is palidore")
else:
    print(a,"is not palindore")          # chenna is not palindore


# 2

num = int(input("Enter a number: "))
rev = 0
temp = num

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if num == rev:
    print(num, "is a Palindrome")
else:
    print(num, "is NOT a Palindrome")




# same as reverse