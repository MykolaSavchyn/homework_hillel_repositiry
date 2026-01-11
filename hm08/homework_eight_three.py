def find_unique_value(some_list:list):
    some_dict = {}
    for i in some_list:
        if i not in some_dict:
            some_dict[i] = 1
        else:
            some_dict[i] = some_dict[i] + 1

    for key, value in some_dict.items():
        if value == 1:
                return key

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")