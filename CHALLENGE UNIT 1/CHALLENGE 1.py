def fact(n):
 if n==0 or n==1:
  return 1
 else:
  return n*fact(n-1)

number=3
res=fact(number)

print('factorial of{} is {}'.format(number,res))