"""
Problem Statement: Permutation Sequence
The set [1, 2, 3, ..., n] contains a total of n! unique permutations. By listing and labeling all of the 
permutations in order, we get the following sequence for n = 3: '123', '132', '213', '231', '312', '321'. 
Given n and k, return the kth permutation sequence.
"""

def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)
def kth_permutation(n, k):
    my_array = [ele for ele in range(1,n+1)]
    kth_permutaion = []
    while len(my_array)>0:
        factorial_of_array_len = factorial(len(my_array)-1) #selecting the subset of the array to be used for the next element in the permutation
        next_ele_index = k//factorial_of_array_len #selecting the index of the next element in the permutation
        kth_permutaion.append(my_array.pop(next_ele_index)) #removing the element from the array and adding it to the permutation
        k %=  factorial_of_array_len #updating k to be the index of the next element in the permutation(in the subset of the array)

    return kth_permutaion


print(kth_permutation(4, 17))



    
