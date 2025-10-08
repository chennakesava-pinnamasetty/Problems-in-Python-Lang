

n = int(input('Enter a number : '))

sqrt = int(n ** 0.5)

if sqrt * sqrt == n:
    print(f"{n} is a perfect square.")
else:
    print(f"{n} is not perfect square. ")



'''
2️⃣ sqrt = int(n ** 0.5)

Here we are finding the square root of n.

n ** 0.5 means "raise n to the power of 0.5" → which is the same as taking the square root.

Example: 16 ** 0.5 = 4.0

Then we use int() to remove the decimal and store only the integer part.

So sqrt = 4.

3️⃣ if sqrt * sqrt == n:

We square the integer square root (sqrt * sqrt) and check if it is equal to the original number.

This step verifies whether the number is a perfect square.

Example:

For n = 16: sqrt = 4

sqrt * sqrt = 4 * 4 = 16

Since 16 == 16, it’s a perfect square ✅

Counter Example:

For n = 20: sqrt = 4

sqrt * sqrt = 4 * 4 = 16

Since 16 != 20, it’s not a perfect square ❌

'''