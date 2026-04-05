"""
Problem Statement: Count Inversions
Given an array of integers. Find the Inversion Count in the array. 
Inversion Count indicates how far (or close) the array is from being sorted. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
"""

# Time Complexity: O(N) where N is the total length of array_1 and array_2
# Space Complexity: O(N) since we allocate a new list to store the merged results
def sort_two_sorted(array_1, array_2):
    # This acts as the standard merge routine in a Merge Sort. 
    # It takes two sorted sub-arrays, uses two pointers to compare elements, and merges them into a single sorted array.
    result = []
    pointer_1, pointer_2 = 0, 0

    while pointer_1 < len(array_1) and pointer_2 < len(array_2):
        if array_1[pointer_1] < array_2[pointer_2]:
            result.append(array_1[pointer_1])
            pointer_1 += 1
        else:
            result.append(array_2[pointer_2])   # ✅ fixed this
            pointer_2 += 1

    if pointer_1 != len(array_1):
        result.extend(array_1[pointer_1:])
    else:
        result.extend(array_2[pointer_2:])

    return result


# Time Complexity: O(N * M) where N and M are the lengths of array_2 and array_1.
# Space Complexity: O(1) as we just increment a counter iteratively.
def counter(array_1, array_2):
    # This is an unoptimized nested-loop matching process to count inversions across two arrays.
    # We find how many elements in the left sorted array are strictly greater than a given element in the right sorted array.
    count = 0
    for i in range(len(array_2)):
        for j in range(len(array_1)):
            if array_1[j] > array_2[i]:
                count += (len(array_1) - j)
                break   # ✅ important to avoid overcounting
    return count


# Time Complexity: O(N log N * N) due to the unoptimized counter logic spanning across the recursion tree layers.
# Space Complexity: O(N) for both the execution stack and the extra temporary arrays built on return.
def helper(my_array):
    # Main driver for counting valid inversions. We divide the array using Merge Sort logic 
    # and compute the inversions at each cross-merge step using the counter() function.
    count = 0

    # Time Complexity: Basic Merge Sort reduction tree depth of O(log N).
    # Space Complexity: O(N) spanning recursive splits tracking independent arrays.
    def count_inversion(my_array):
        nonlocal count   # 🔥 this is what you wanted

        if len(my_array) == 1:
            return my_array

        mid = len(my_array) // 2
        left_sorted = count_inversion(my_array[:mid])
        right_sorted = count_inversion(my_array[mid:])

        count += counter(left_sorted, right_sorted)

        return sort_two_sorted(left_sorted, right_sorted)

    count_inversion(my_array)
    return count

#problem to count the number of paira (i,j) such that i<j and arr[i]>arr[j]
print(helper([1,2,3,4]))        # 0
print(helper([2,4,1,3,5]))     # 3