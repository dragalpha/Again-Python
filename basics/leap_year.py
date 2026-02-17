def is_leap(year):
    if(year%4==0 and year%100 != 0):
        print("True")
    elif(year%400 == 0):
        print("True")
    else:print("False")
    
year = int(input())
print(is_leap(year))