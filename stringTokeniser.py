import re
# String Tokenizer
String ='Krishna.kumar,1994,08,23,male'

#splitinf the string using ','
tokens = re.findall(r"[\w]+",String)
firstName = tokens[0]
lastName = tokens[1]
DOB = (int(tokens[2]),int(tokens[3]),int(tokens[4]))
isMale = (tokens[5] == 'male')
print firstName+' '+lastName
print DOB
print isMale
