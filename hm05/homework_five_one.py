# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True


import keyword
import string

you_variable = input("Please enter your variable: ")
punc_marks = string.punctuation.replace("_", " ")
counter = 0

for i in you_variable:
    if i in punc_marks:
        counter += 1

if (counter > 0
    or you_variable[0].isdigit()
    or (any (c.isalpha() for c in you_variable) and not you_variable.islower())
    or you_variable in keyword.kwlist
    or (not any (c.isalpha() for c in you_variable) and you_variable.count('_')>1)):
    print(False)
else:
    print(True)








