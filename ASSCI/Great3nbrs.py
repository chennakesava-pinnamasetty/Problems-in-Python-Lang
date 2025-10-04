
# 1
a = 10
b = 20
c = 40
d = 30
print("The smallest nbrs is :",min(a,b,c,d))        # The smallest nbrs is : 10
print("The great nbr is :",max(a,b,c,d))           # The great nbr is : 40

print()

# 2
a = [1,2,3,6,4]
print("The smallest nbrs is :",min(a))          # The smallest nbrs is : 1
print("The great nbr is :",max(a))              # The great nbr is : 6



# 3
a = 10
b = 20
c = 30

if a >=b and a <=c:
    print(a)
elif b <= c and b <= a:
    print(b)
else:
    print(c)            # 30


print()

# 4

nms = list(map(int,input("Enter a some nbrs saparatly :").split()))

print("The great nbr is :",max(nms))
print("The smallest nbr is :",min(nms))
 
                           # Enter a some nbrs saparatly :11 3 55 90 22
                           # The great nbr is : 90
                           # The smallest nbr is : 3