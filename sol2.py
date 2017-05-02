string1 =raw_input()
string1= string1.lower()
string2 = raw_input()
string2 = string2.lower()
str1=''
str2=''
for s in string1:
    if s.isalnum():
        str1 = str1 + str1.join(s);
for s in string2:
    if s.isalnum():
        str2 = str2 + str2.join(s);
str1 = sorted(str1)
str2= sorted(str2)
if str1 == str2:
    print "anagram"
else:
    print "not anagram"
 
