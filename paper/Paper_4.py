
'''

In an array, a superior element is one which is greater than all the elements to its right side. The rightmost element itself be a superior element.

You are given a function,

int Find_Number_Of_Superior_Element(int arr[], int n);

The function accepts an integer array and the size of array, Implement the function to find the total number of superior elements present in array.

Assumptions:

N>0 and Array index starts from 0

Input

: n= 6 arr= [8,10,6,2,9,7]

Output: 3



'''

def Find_Number_Of_Superior_Element(arr, n):
    count = 0
    max_from_right = float('-inf')
    
    # Traverse from right to left
    for i in range(n-1, -1, -1):
        if arr[i] > max_from_right:
            count += 1
            max_from_right = arr[i]
    
    return count


# Example
arr = [8, 10, 6, 2, 9, 7]
n = len(arr)
print(Find_Number_Of_Superior_Element(arr, n))  # Output: 3


'''
Step-by-step Check

8 → Right side: [10, 6, 2, 9, 7] → 10 > 8 → Not superior ❌

10 → Right side: [6, 2, 9, 7] → 10 > all of them → Superior ✅

6 → Right side: [2, 9, 7] → 9 > 6 → Not superior ❌

2 → Right side: [9, 7] → 9 > 2 → Not superior ❌

9 → Right side: [7] → 9 > 7 → Superior ✅

7 → No right side → Always superior ✅
'''





def superior(int,arr):
    count = []

    for i in range(n-1,-1,-1):
        if 