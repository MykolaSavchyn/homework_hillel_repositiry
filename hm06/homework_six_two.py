a = 60
b = 60*60
c = 60*60*24

d = int(input("Please enter a digit:  "))
days = d//c
hours = ((d%c)//b)
minutes = (((d%c)%b)//a)
seconds = (((d%c)%b)%a)

str_days = str(days)
tup = ('0', '5', '6', '7', '8', '9')

if (days >= 11 and days <= 20) or str_days[-1] in tup:
    k = 'днів'
elif str_days[-1] == '1':
    k = 'день'
else:
    k = 'дні'

print(f'{d} -> {days} {k}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')




