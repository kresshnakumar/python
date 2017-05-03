def binary_search(container,ele):
    i = 0
    j = len(container) -1
    while i < j:
        middle = (i + j)/2
        if container[middle] < ele:
            i = middle+1
        else:
            j = middle
    if container[i] == ele:
        return i
    else:
        return -1
lst = range(0,50,5) #this will produce the elements(0,5,10,15...45)
num = 15
index = binary_search(lst,num)
if index >=0:
    print str(num)+' found at index :'+str(index)
else:
    print str(num)+' not found'
