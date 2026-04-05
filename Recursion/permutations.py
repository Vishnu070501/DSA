"""
Problem Statement: Permutations
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
"""

def permutations(arr):
    if len(arr) ==1:
        return [arr]
    
    roap = permutations(arr[1:])
    result = []
    for ele in roap:
        for i in range(0,len(ele)+1):
            ele.insert(i,arr[0])
            result.append([*ele])
            ele.pop(i)
    return result

def permutations_optimised(arr,res=[],map={}):
    if all(map.get(ele) for ele in map.keys()):#if all keys picked and stored in our res print it
        print(res)
        return
    for ele in arr:
        if map.get(ele)==False:#if not picked 
            res.append(ele)#pick it
            map[ele]=True#mark it
            permutations_optimised(arr,res,map)# and make the recursive call for rest of the elements
            res.pop()#backtracking(because )
            map[ele]=False

def permutations_more_opt(arr, solvable_ind):#here the solvable index means the index we solvin plus it also denotes that elements before this index have been set in our perm
    if solvable_ind == len(arr):
        print(arr)
        return
    for i in range(solvable_ind, len(arr)):#you cant swap from solvable+1 as the recursive call for the og element at solvable also has to go,also when you set this to go from solvable_ind+1 at the last element the call for base case won't go(as then we won't enter the loop(i becomes outta range)to make solvable_ind ==len(arr)) and it won't print(always try to analyse recursion using the euler path not the debugger)
        arr[solvable_ind],arr[i] = arr[i],arr[solvable_ind]
        permutations_more_opt(arr, solvable_ind+1)# iss point pe in the loop ye solvable index solve(we have set ith eleement at solvable index) ho gaya h solve for the next solvable ind
        arr[solvable_ind],arr[i] = arr[i],arr[solvable_ind]# back track for next genuine swap


# print(permutations([1,2]))
my_array = [1,2,3]
# permutations_optimised(my_array, [], {val:False for _,val in enumerate(my_array)})
permutations_more_opt([1,2,3],0)

# d = dict.fromkeys(arr, 0)
# d = {val: idx for idx, val in enumerate(arr)}

