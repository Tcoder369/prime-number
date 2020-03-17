import time
import random
print('this is a prime number checker. it checks if your number is prime or not')
print('please put in only natural numbers')
print('putting in letters will result in an error')
print('putting in math expressions like 5+8 or 5^4 will also result in an error')
print('putting in symbols of any kind will also result in an error')
      
while True:
  up_to_n=[]
  def figure_if_prime(): 
      time.sleep(11)
      print()
      n=int(input('which number do you want to check?'))
      for i in range(2,n):
        up_to_n.append(i)
      if n == 0:
        print('zero is zero. not cosidered prime or not prime')
      for i in up_to_n:
          if n%i == 0:
            print()
            print('calculating...')
            time.sleep(random.randint(2,4))
            print(str(n) + ' is divisible by ' +str(i)+ ' ,not prime')
            break
          elif i == n-1 and n%i != 0:
            print()
            print('calculating...')
            time.sleep(random.randint(2,4))
            print(str(n) +' is prime')
      print()
      time.sleep(3)
  figure_if_prime()