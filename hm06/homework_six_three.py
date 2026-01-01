
digit_res = int(input("Please enter your digit: "))
digit_start = digit_res

while digit_res > 9:
    d = 1
    for i in str(digit_res):
        d = d * int(i)
    digit_res = d
print(f'{digit_start} -> {digit_res}')

