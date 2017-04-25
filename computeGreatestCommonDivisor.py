import math 
def computeGCD(a,b):
  if a >= b:
    res = calulateGCD(b,a)
  else:
    res = calulateGCD(a,b)
  
  return res 

def calulateGCD(a,b):
  #assume a is no bigger than b 
  limit = int(math.sqrt(a))
  gcd = 1 
  i = 1
  while i <= limit:
    if a % i == 0: 
      divisor = a // i 
      if b % divisor == 0:
        gcd = divisor
        break 
      elif b % i == 0: 
        gcd = i 
      else: 
        pass 
    i += 1 
  return gcd 
