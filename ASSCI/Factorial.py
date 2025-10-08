
# 1

n = int(input("Enter a number : "))

fact = 1
for i in range(1,n+1):
    fact *= i
print("The factoroial :",fact) 


'''
Input: 5

Calculation: 1×2×3×4×5 = 120

Output: The factorial of 5 is: 120
'''



# 2


while True:
    n = int(input("Enter a number : "))
    if n == -1:
        break

    fact = 1
    for i in range(1,n+1):
     fact *= i
    print(f"THe Fibanacci {n} nbrs :",fact)
