year = int(input("Please tell your year :-"))
if year %100 ==0 and year % 400 == 0:
    print("leap year")

elif year %100 != 0 and year %4 == 0:
    print("leap year")
else : 
    print("not a leap year")