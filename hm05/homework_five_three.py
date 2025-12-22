# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string

your_variable = input("Please enter your variable: ")

your_variable = your_variable.title()

your_variable_1= ""
for i in your_variable:
    if i not in string.punctuation and i != " ":
        your_variable_1 = your_variable_1+i

your_variable_1 = "#"+your_variable_1

if len(your_variable_1)>140:
    your_variable_1 = your_variable_1[:140]

print(your_variable_1)

