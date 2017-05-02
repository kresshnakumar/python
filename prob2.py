import re
str = "crap built on lies."
s = ''
s.join(e for e in str if e.isalnum())
print s

#string = "Special $#! characters   spaces 888323"
#''.join(e for e in string if e.isalnum())

