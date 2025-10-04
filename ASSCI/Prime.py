
# 1

num = int(input("Enter a nbr : "))

if num > 1:
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            print(num,"is not prime number ")
            break
    else:
        print(num,"is prime number ")
else:
    print(num,"is not prime")


                     # Enter a nbr : 3
                     # 3 is prime number 


# 2

start = int(input('Enter tart prime nbr : '))
end = int(input("Enter end prime nbr : "))

print("Prime nbers between",start,"and",end,":")

for num in range(start,end+1):
    if num > 1:
        for i in range(2,int(num ** 0.5)+1):
            if num % i == 0:
                break
        else:
                print(num,end=" ")

      #  Enter tart prime nbr : 2
      #  Enter end prime nbr : 20
      #  Prime nbers between 2 and 20 :
      #  2 3 5 7 11 13 17 19
print()

n = int(input("Enter a number :"))
for i in  range(2,n):
    if (n%i) == 0:
        print("Not prime")
        break
    else:
        print(n,"prime nbr ")