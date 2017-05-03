# Buble Sort Algorithm

def buble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    

lst = [3,1,7,4,9,2,5,6]
print 'unsorted list :',lst
buble_sort(lst)
print 'sorted list :',lst
