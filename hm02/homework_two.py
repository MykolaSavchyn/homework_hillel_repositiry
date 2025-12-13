
# task_two_one (I think it is better to use type float)

print("task_two_one about squared number ")
number=float(input("Enter your number: "))
print("squared number is", number**2)
print("____________________________________")


# task_two_two

print("task_two_two arithmetic mean")
a = float(input("Enter your first number: "))
b = float(input("Enter your first number: "))
c = float(input("Enter your first number: "))
print("arithmetic mean is: ", (a+b+c)/3)
print("____________________________________")


# task_two_three

print("task_two_three about time")
minutes = int(input("Enter number of minutes: "))
div, mod =divmod(minutes,60)
print("It will be ", div, "hours and ", mod, "minutes")
print("____________________________________")


# task_two_four

print("task_two_four about price and discount")
price = int(input("Enter your price %: "))
discount = int(input("Enter your discount: "))
print("Price with discount will be: ", price-(price*discount/100))
print("____________________________________")


# task_two_five

print("task_two_five about last digit of number")
numb = int(input("Enter your number : "))
print("Last digit of your number is: ", numb%10)
print("____________________________________")

# task_two_six

print("task_two_six about perimeter of a rectangle")
length=int(input("Enter length : "))
width=int(input("Enter width : "))
print("Perimeter of a rectangle is: ", (length+width)*2)
print("____________________________________")

# task_two_seven

print("task_two_seven about number in colu")
num = int(input("Enter your number : "))
print(num//1000)
o=(num%1000)
print(o//100)
s=o%100
print(s//10)
print(s%10)
print("____________________________________")