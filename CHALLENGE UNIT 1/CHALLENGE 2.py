def leap(year):
 if(year%4==0 and year%100!=0) or year%400==0:
     return True
 else:
     return False

year=2024
if leap(year):
   print('{}is a leap year'.format(year))
else: 
   print('{}is not a leap year'.format(year))
 