

start = int(input("Enter starting Number : "))
end = int(input("Enter ending number : "))

print(f"Armstrong number {start} and {end} are : ")

for num in range(start , end + 1):
    order = len(str(num))

    sum_of_digits = sum(int(digits) ** order for digits in str(num))

    if num == sum_of_digits:
        print(num)