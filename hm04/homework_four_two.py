# [1, 3, 5] => 30
# [6] => 36
# [] => 0
# [0, 1, 7, 2, 4, 8] => 88

my_list = [0, 1, 7, 2, 4, 8]

my_list_pair = []

if len(my_list) == 0:
    print(my_list, len(my_list), sep=' => ')
else:
    for ind, item in enumerate(my_list):
        if ind%2 == 0:
            my_list_pair.append(item)
    # print(my_list_pair)
    print(my_list, sum(my_list_pair)*my_list[-1], sep=' => ')
