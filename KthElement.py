#Andrew Lee
#CS 325
#Assignment 2: KthElement.py, a function that recursively returns the kth element in a combined array
#Due Date: January 23, 2023


def kthElementHelper(arr, start, end, k):
    '''helper function that recursively divides our array until we find the kth position. Similar to a binary search.'''
    mid = (start + end) // 2
    if k == mid:
        return arr[mid-1]                                   #to account that kth position starts at 1, not zero
    if k > mid:
        return kthElementHelper(arr, mid+1, end, k)
    if k < mid:
        return kthElementHelper(arr, start, mid-1, k)

def kthElement(Arr1, Arr2, k):
    '''function that combines two given arrays and returns the value at the kth position'''
    combined_array = []
    while len(Arr1) > 0 and len(Arr2) > 0:                  #while loop that combines the two arrays
        if Arr1[0] <= Arr2[0]:
            combined_array.append(Arr1[0])
            Arr1 = Arr1[1:]
        else:
            combined_array.append(Arr2[0])
            Arr2 = Arr2[1:]
    #if k < 0 or k > len(combined_array):                    #cases where k is an invalid target
    #    return False
    return kthElementHelper(combined_array, 1, len(combined_array), k)