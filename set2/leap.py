year = int(input("Enter a year A.D.: "))
if ((year % 4 == 0) and not(year % 100 == 0)) or (year%400 == 0):
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")
