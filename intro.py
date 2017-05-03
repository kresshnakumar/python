#python numbers
age = 23
pi = 3.14159

# Python Strings

string = 'Krishna Kumar'
tokens = string.split() #splits string on space and return parts

# tokens after splittimg

first_name = tokens[0]
last_name = tokens[1]

#String Concatination
name = first_name + '' + last_name

# 'if' Statement
if(string == name):
    print (' Strings are matching')
else:
    print 'String\'s not matched'

# Python Lists
students = ['krishna','kumar','gaddam']
students.append('kannaya') # insert another item into list

#for loop

for stu in students:
    print 'hello! '+stu
# Python Tuple [Immutable sequence]
ages = (21,22,23)

# Python sets [No order, no duplicates]
uniqueAges = set(ages)
uniqueAges.add(21) #already in set, so no effect
for ag in uniqueAges:
    print ag
uniqueAges.remove(21) # removing from set
for ag in uniqueAges:
    print ag
#testing set membership
if 22 in uniqueAges:
    print 'found'
else:
    print 'not found'

# Sorting
students.sort() # in-place sort
for stu in students:
    print 'hello! '+stu
order = sorted(uniqueAges) #sorting results in new list

#python Dictionary
netWorth = { }
netWorth['Trump'] = 30000000
netWorth['obama'] = 50000000
netWorth['gatess'] = 40000000
netWorth['joe'] = 6000000
#iterating over key-value pairs
for (person,worth) in netWorth.items():
    if worth <= 30000000:
        print '<30000000'
#testing dictionary membership
if 'Trump' in netWorth:
    print'present'
