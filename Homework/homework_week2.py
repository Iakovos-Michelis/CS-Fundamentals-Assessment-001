year = int(input("Give a year:"))

if (year % 4 != 0):
    print("Year :",year,"is not a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("Year :",year,"is a leap year")
elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 !=0):
    print("Year :",year,"is not a leap year")
elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 ==0):
    print("Year :",year,"is a leap year")