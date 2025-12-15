# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

list_initial = [1, 2, 3, 4, 5, 6]
# list_initial = [1, 2, 3]
# list_initial = [1, 2, 3, 4, 5]
# list_initial = [1]
# list_initial = []

size = len(list_initial)

if size == 0:
    list_1 = list_initial
    list_2 = list_initial
    list_initial = [list_1, list_2]
    print (list_initial)
else:
    if (size%2) == 0:
        list_1 = list_initial[:int(size/2)]
        list_2 = list_initial[int(size/2):]
        list_initial = [list_1, list_2]
        print(list_initial)
    else:
        list_1 = list_initial[:int((size // 2)+1)]
        list_2 = list_initial[int((size // 2)+1):]
        list_initial = [list_1, list_2]
        print(list_initial)

