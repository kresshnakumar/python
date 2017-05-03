def linear_search(container,ele):
    for i in range(len(container)):
        if container[i] == ele:
            print ele +" found"
            return i
    return -1
lst = [4,2,5,7,9,1,3]
element = 10
index = linear_search(lst,element)
print 'Found '+str(element)+' at index :'+str(index)
