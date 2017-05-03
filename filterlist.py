sample_list = [25, 'Krishna',38,'Kumar',54,'Gaddam']

def filter_marks(lst):
    integers = []
    rest = []

    for ele in lst:
        if type(ele) is int: #type will return type of element
            integers.append(ele)
        else:
            rest.append(ele)
    #multiple comma seperated values are returned as tuple in python
    return integers, rest

#tuple result from fuction can be unpacked
integers, rest = filter_marks(sample_list)
print integers
print rest
