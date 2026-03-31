def merge_sort(arr):
    if(len(arr)==1):
        return arr

    print(len(arr)//2)
    first_half_sorted = merge_sort(arr[:len(arr)//2])
    second_half_sorted = merge_sort(arr[len(arr)//2:])


    return merge(first_half_sorted, second_half_sorted)

def merge(arr1,arr2):

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