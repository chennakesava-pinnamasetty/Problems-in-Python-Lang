

#  A leap year is a year that:
#  
#  Is divisible by 4,
#  
#  But not divisible by 100,
#  
#  Except if it is also divisible by 400.


# 1

year = int(input("Enter a year : "))

if ( year % 4 == 0) or (year % 400 == 0 and year % 100 != 0):
    print(year,'Is Leap Year')
else:
    print(year,"Is not leap year")



# 2

start = int(input("Enter start year : "))
end = int(input("Enter end year : "))

print("Leap year between ",start,"and",end,":")

for year in range(start,end +1):
    if ( year % 4 == 0) or (year % 400 == 0 and year % 100 != 0):
        print(year,end=" ")