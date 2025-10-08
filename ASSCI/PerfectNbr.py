

# This is based on factors 

n = int(input("Enter a number : "))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print(f"{n} is perfect nbr ")
else:
    print(f"{n} is not perfect nbr")





'''
Step-by-Step Detailed Explanation:
🟩 1️⃣ Input a number
n = int(input("Enter a number : "))


The program first asks the user to enter a number.

input() reads it as a string, and int() converts it into an integer.

✅ Example:
If you type 6, then
n = 6

🟩 2️⃣ Initialise a variable
sum = 0


Here we create a variable sum to store the total of all divisors (numbers that divide n exactly).

Initially, sum is 0 because we haven’t found any divisors yet.

🟩 3️⃣ Loop through all possible divisors
for i in range(1, n):


range(1, n) → generates all numbers from 1 to n-1.

We don’t include n itself because a number’s proper divisors exclude the number.

✅ Example:
If n = 6, this loop checks:
i = 1, 2, 3, 4, 5

🟩 4️⃣ Check if i divides n exactly
if n % i == 0:


% is the modulus operator (gives remainder).

If the remainder is 0, it means i divides n perfectly.

✅ For n = 6:

6 % 1 == 0 → yes
6 % 2 == 0 → yes
6 % 3 == 0 → yes
6 % 4 == 2 → no
6 % 5 == 1 → no


So, divisors = 1, 2, 3

🟩 5️⃣ Add each divisor to the total
sum = sum + i


Every time a divisor is found, it’s added to the running total sum.

✅ Continuing with n = 6:

sum = 0 + 1 = 1  
sum = 1 + 2 = 3  
sum = 3 + 3 = 6


Final sum = 6

🟩 6️⃣ Compare the sum with the original number
if sum == n:


If the total of all divisors equals the original number,
it’s a Perfect Number.

✅ For n = 6:
sum = 6, and n = 6 → ✅ Perfect number.

❌ For n = 8:
Divisors = 1, 2, 4 → sum = 7 → ❌ Not perfect.

🟩 7️⃣ Display result
print(f"{n} is perfect nbr ")


or

print(f"{n} is not perfect nbr")


Depending on the condition, it prints whether the number is perfect or not.

🧾 Example Outputs:
Example 1:
Enter a number : 6
6 is perfect nbr

Example 2:
Enter a number : 10
10 is not perfect nbr

💡 Extra Explanation:

Perfect Numbers are very rare.
The smallest few are:

6, 28, 496, 8128, 33550336


They have a unique mathematical property:
they are equal to the sum of their divisors (excluding the number itself).

'''




n = int(input("Enter a number : "))
sum = 0

for i  in range (1,n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print(f"{n} is perfect nbr ")
else:
    print(f"{n} is not perfect nbr")



