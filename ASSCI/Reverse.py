

a = [1,2,3,4,5]
print(a[::-1])           # [5, 4, 3, 2, 1]




# Reverse an Integer Number

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10        # get last digit
    rev = rev * 10 + digit  # build reverse
    num = num // 10         # remove last digit

print("Reversed number:", rev)




# Reverse all numbers in a list

num = [123,456,789]

reverse = [int(str(n)[::-1]) for n in num]
print("Reversed Nbrs :",reverse)            # Reversed Nbrs : [321, 654, 987]



# Explanation :

'''
1️⃣ numbers = [123, 456, 789]

This creates a list of numbers.

A list is like a container holding multiple items: [123, 456, 789].


2️⃣ for n in numbers

This is a for loop that goes through each number in the list.

First iteration → n = 123

Second iteration → n = 456

Third iteration → n = 789


3️⃣ str(n)

str() converts the number to a string.

Example: 123 → "123"

We convert to a string because strings can be reversed easily in Python.


4️⃣ [::-1]

This is Python slicing for reversing a string.

"123"[::-1] → "321"

It reads the string from end to start.


5️⃣ int(...)

Converts the reversed string back to an integer.

"321" → 321


6️⃣ [int(str(n)[::-1]) for n in numbers]

This is a list comprehension.

It creates a new list by reversing each number in numbers.

Step by step for our list:

123 → "123" → "321" → 321

456 → "456" → "654" → 654

789 → "789" → "987" → 987

Result → [321, 654, 987]


7️⃣ print("Reversed numbers:", reversed_list)

Prints the new list of reversed numbers.

Output:

Reversed numbers: [321, 654, 987]'''




nbr = [123,456,789]

reverse = [int(str(n)[::-1]) for n in nbr]
print(reverse)



