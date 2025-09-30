
# 1
num = "4" + "2"
val = int(num) + 6
print(val) 
                         # 48

# 2
a = "2"
b = 3
print(a * b)       # 222

# 3
food = "Pizza"
if food[0] == "P":
    print("Order Confirmed")
else:
    print("Order Pending")       # Order Confirmed


# 4
temps = [32,35,28,40,30]
print(min(temps),max(temps))     # 4


# 5
a = ["p" "y" "t" "h" "o" "n"]
b = a[0]
print(b)      # python


a = ["p", "y" ,"t", "h", "o" ,"n"]
b = a[0]
print(b)     # p



# 6
a = 5
b = 2
c = 5 * 2 + 3
a += 13 - 2
print(a)       # 16


# 7
total = 0
for i in range(4):
    total += i
    print(total)
                    # 0
                    # 1
                    # 3
                    # 6


# 8 
 # This infinite loop
'''
while 1:
    try:
        print("Hello",end=" ")
    finally:
        print("World")'''


# 8
num = [1,2,3,4,5]        # 1+2+3+4+5
print(sum(num))       # 15


# 9

num = [1,2,3,4,5]
for i in range(len(num)):
    print(f"the index {i}and num is {num}")
print("The total is:",len(num))


# the index 0and num is [1, 2, 3, 4, 5]
# the index 1and num is [1, 2, 3, 4, 5]
# the index 2and num is [1, 2, 3, 4, 5]
# the index 3and num is [1, 2, 3, 4, 5]
# the index 4and num is [1, 2, 3, 4, 5]
# The total is: 5


num = [1,2,3,4,5]
for i in range(len(num)):
    print(f"the index {i}and num is {num[i]}")
print("The total is:",len(num))

# the index 0and num is 1
# the index 1and num is 2
# the index 2and num is 3
# the index 3and num is 4
# the index 4and num is 5
# The total is: 5