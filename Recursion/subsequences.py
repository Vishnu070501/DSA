"""
Problem Statement: Subsets / Subsequences
Given an integer array nums of unique elements, return all possible subsets (the power set). 
The solution set must not contain duplicate subsets. Return the solution in any order.
"""

def subsequences(arr):
    if len(arr)==1:
        return [[],arr]
    subseq_wo_first_ele = subsequences(arr[1:])
    # print(subseq_wo_first_ele) 
    subseq_w_first_ele = [[arr[0],*ele] for ele in subseq_wo_first_ele]
    return [*subseq_wo_first_ele,*subseq_w_first_ele]

#these kinds of recursive calls where it returns nothing the result is ussually stored in the call stack(so either return or store sumn in a var in callstack or both)
#whatever you are feeling neccessary that should be stored in the stack that can represent our choices like result matrix on the euler path you can store ,and even we can store result data structures that we can push our correct answers, also we can store state variables like solving indexes which can represent the current stage we are at the euler path
#you can't get a high level thinking analogy(its a lil bit difficult)
# (you have to dry run a low level thinking for a small case)
# in the euler path the edges pe jo kaam ho rha h usse matlab h
def subseq_opt(arr, solve_ind=0, res=None):
    if res is None:
        res = [[]]

    if solve_ind == len(arr): #if the index of the element being solved reaches beyond array print the result
        print(res)
        return

    new_subseq = [ele + [arr[solve_ind]] for ele in res]
    print(f"with solvable :{new_subseq}, w/o solvable:{res}")
    res.extend(new_subseq)
    print(f"new result combined: {res}")

    subseq_opt(arr, solve_ind + 1, res)

def subseq_opt2(arr, solve_ind, subseq_res):#here we build an item of the subsequence result
    if solve_ind == len(arr):#when the index of the solvable is beyond our array means we have built a subsequence item just print it 
        print(subseq_res)
        return

    # Excluding arr[ind] in our result ka recursive call
    subseq_opt2(arr, solve_ind + 1, subseq_res)

    # Include arr[ind] in our result array ka recursive call
    subseq_res.append(arr[solve_ind])
    subseq_opt2(arr, solve_ind + 1, subseq_res)
    subseq_res.pop()   # backtrack(because this result represents our choices at each element in euler)


    
# print(subsequences([1,2,3]))


# subseq_opt([1,2,3])
subseq_opt2([1, 2, 3], 0, [])
