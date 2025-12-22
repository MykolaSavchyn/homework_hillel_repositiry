cont = 'y'

while cont == 'y':

    figure_one = float(input("Please enter first figure: "))
    sign = input("Please enter the sign +, -,*,: ")
    figure_two = float(input("Please enter second figure: "))


    if sign == "+":
        res = figure_one + figure_two
        print("result is: ", res)
    elif sign == "-":
        res = figure_one - figure_two
        print("result is: ", res)
    elif sign == "*":
        res = figure_one * figure_two
        print("result is: ", res)
    elif sign == "/" and figure_two != 0:
        res = figure_one / figure_two
        print ("result is: ", res)
    elif sign == "/" and figure_two == 0:
        print ("figure_two can not be 0 for '/'")
    else:
        print("You have entered wrong value")

    cont = (input("Do you want to continue? (y/n): "))




