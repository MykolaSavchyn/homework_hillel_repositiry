# our_list = [12, 3, 4, 10]
# our_list = [1]
# our_list = []
our_list = [12, 3, 4, 10, 8]

size = len(our_list)

if size>0:
    last_element = our_list.pop()
    our_list.insert(0, last_element)
    print(our_list)
else:
    print([])