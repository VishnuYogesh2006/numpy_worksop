#write a program to find the sum of digits of a given number'
def sumDigits(no):
    return 0 if no == 0 
  else int(no % 10) + sumDigits(int(no/10))
print(sumDigits(687)
