"""
Problem Statement: Count Inversions
Given an array of integers. Find the Inversion Count in the array. 
Inversion Count indicates how far (or close) the array is from being sorted. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
"""

def sort_two_sorted(array_1, array_2):
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


def counter(array_1, array_2):
    count = 0
    for i in range(len(array_2)):
        for j in range(len(array_1)):
            if array_1[j] > array_2[i]:
                count += (len(array_1) - j)
                break   # ✅ important to avoid overcounting
    return count


def helper(my_array):
    count = 0

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