# Selection Sort

def find_smallest(lst,start):
    small = start
    for j in range(start + 1,len(lst)):
        if lst[j] < lst[start]:
            small = j
    return small

def selection_sort(lst):
    for i in range(len(lst)):
        smallest = find_smallest(lst,i)
        if smallest !=i:
            lst[smallest],lst[i] = lst[i],lst[smallest]

lst = [2,6,4,1,7,9]
selection_sort(lst)
print lst
