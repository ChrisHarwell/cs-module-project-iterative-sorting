from math import floor

def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    n = len(arr)
    L = 0
    R = n-1
    
    while L <= R:
        mid = floor((L+R)/2)
        if arr[mid] < target:
            L = mid + 1
        elif arr[mid] > target:
            R = mid - 1
        else:
            return mid
    return -1  # not found
