

def search(a):
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")

a = int(input("Enter a number :"))

print(search(a))

                                # Even
                                # None



b = int(input("Enter a number : "))

if b % 2 == 0 :
    print(f"{b} is even")
else:
    print(f"{b} is Odd")
                                   # Enter a number : 22
                                   # 22 is even



# Even

even = []

for i in range(1,21):
    if i % 2 == 0:
        
        even.append(i)

print(even)               # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



# Odd

odd = []

for i in range(1,21):
    if i % 2 != 0:
        odd.append(i)
print(odd)               # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]




# Even & Odd

Even = []
Odd = []

for i in range(1,21):
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)

print(Even)        # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(Odd)         # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]






start = int(input("Enter a starting nbr : "))
end = int(input("Enter a ending nbr : "))

Even = []
Odd = []

for i in range(start,end + 1):
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)

print(Even)       
print(Odd)  

                    # Enter a starting nbr : 12
                    # Enter a ending nbr : 30
                    # [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
                    # [13, 15, 17, 19, 21, 23, 25, 27, 29]