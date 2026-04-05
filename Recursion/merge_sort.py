"""
Problem Statement: Merge Sort
Given an array of integers, sort the array in ascending order using the Merge Sort algorithm.
"""

# Time Complexity: O(N log N) consistently dividing the arrays logarithmically into fundamental units.
# Space Complexity: O(N) deep-copying arrays inside slices dynamically alongside maximum functional depth limit stacking bindings.
def merge_sort(arr):
    # Structurally breaks down recursively splitting collection sizes uniformly in half until atomized parts stand isolated.
    if(len(arr)==1):
        return arr

    print(len(arr)//2)
    first_half_sorted = merge_sort(arr[:len(arr)//2])
    second_half_sorted = merge_sort(arr[len(arr)//2:])


    return merge(first_half_sorted, second_half_sorted)

# Time Complexity: O(N) strictly evaluated spanning linearly the summation length of respective sub-arrays.
# Space Complexity: O(N) to build sequence accumulation structures appending items continuously.
def merge(arr1,arr2):
    # Merges isolated split boundaries by walking two corresponding iterative pointers and transferring values cleanly.

    i,j = (0,0)
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    if i == len(arr1) and j < len(arr2):
        result.extend(arr2[j:])
    elif j == len(arr2) and i < len(arr1):
        result.extend(arr1[i:])
    return result

print(merge_sort([9,8,7,6,5,4,3,2,1]))