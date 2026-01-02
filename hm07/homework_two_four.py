def common_elements():
    list_3 = list()
    list_5 = list()
    for i in range(100):
        if i%3 == 0:
            list_3.append(i)

    for i in range(100):
        if i%5 == 0:
            list_5.append(i)

    set_35 = set(list_3).intersection(set(list_5))
    return set_35

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')