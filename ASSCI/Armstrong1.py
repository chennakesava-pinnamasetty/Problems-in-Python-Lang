

# 1


nbr = int(input("Enter numbers : "))
store = 0
temp = nbr
order = len(str(nbr))

while temp > 0:
    digit = temp % 10

    store += digit ** order
    temp //= 10
if nbr == store:
    print(f"{nbr} is an Armstrong number.")
else:
    print(f"{nbr} is not an Armstrong number.")





# 2


nbr = int(input("Enter a number : "))

order = len(str(nbr))
sum_of_nbr = sum(int(digit) ** order for digit in str(nbr))

if nbr == sum_of_nbr:
    print(f"{nbr} is an Armstrong number.")
else:
    print(f"{nbr} is not an Armstrong number.")



'''How this simpler version works

1. str(num) → changes the number into a string so we can loop over its digits easily.

Example: "153" → digits '1', '5', '3'.

2. len(str(num)) → gives the count of digits.

Example: 3 for 153.

3. sum(int(digit) ** order for digit in str(num))

This is a generator expression that does the job of the while loop in one line:

Converts each digit back to an integer.

Raises it to the power of order.

Adds them all together.

4. Compare with original number → if equal, it’s Armstrong.'''




nbr = int(input("Enter a nbr : "))

order = len(str(nbr))

sum_of = sum(int(digits) ** order for digits in str(nbr))