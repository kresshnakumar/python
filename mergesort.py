# Merge Sort
def merge(left,right):
    result = []

    while len(left)>0 and len(right)>0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    
    return result

def merge_sort(lst):
    if len(lst) <=1:
        return lst
    l = len(lst)
    left = lst[:l/2]
    right = lst[l/2:]
    
    #sort left and right parts
    leftSorted = merge_sort(left)
    rightSorted = merge_sort(right)

    return merge(leftSorted,rightSorted)

lst = [8,2,7,1,4,9,6,5]
merge_sort(lst)
print lst
