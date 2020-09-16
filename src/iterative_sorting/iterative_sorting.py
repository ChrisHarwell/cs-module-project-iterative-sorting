# TO-DO: Complete the selection_sort() function below

def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


def selection_sort(arr):
    # loop through n-1 elements
    for cur_index in range(0, len(arr) - 1):
        smallest_index = cur_index
        for i in range(cur_index, len(arr)):
            if arr[i] < arr[smallest_index]:
                smallest_index = i

        swap(arr, cur_index, smallest_index)

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    first_run = True
    swap_occurred = False

    while first_run or swap_occurred:
        first_run = False
        swap_occurred = False

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                swap_occurred = True
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
