import string

tup = tuple(input('Enter two letters with a hyphen:  '))
st = tup[0]
en = tup[-1]
# print(st)
# print(en)

string_=string.ascii_letters

begin_ind = string_.index(st)
# print(begin_ind)
end_ind = string_.index(en)
# print(end_ind)

my_string = ''
for i in range (begin_ind, end_ind+1):
    my_string += string_[i]
print(f'"{st}-{en}" -> {my_string}')