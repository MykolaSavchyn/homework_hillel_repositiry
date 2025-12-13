figure_one = float(input("Please enter first figure: "))
sign = input("Please enter the sign +, -,*,: ")
figure_two = float(input("Please enter second figure: "))


if sign == "+":
    res = figure_one + figure_two
    print(res)
elif sign == "-":
    res = figure_one - figure_two
    print(res)
elif sign == "*":
    res = figure_one * figure_two
    print(res)
elif sign == "/" and figure_two != 0:
    res = figure_one / figure_two
    print (res)
else:
    print ("figure_two can not be 0 for '/'")
