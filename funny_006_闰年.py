year = "1900"

y = int(year)
if y%4==0 and y%100 != 0 or y%400 ==0:
    print(366)
else:
    print(365)
