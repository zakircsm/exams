x=[]
n=int(input('no of random numbers:'))
import random
for i in range(n):
    x.append(random.randint(1,101))
print(x)
print('average:',sum(x)/n)
x.sort()
print(x)
print('min:',x[0])
print('max:',x[n-1])
print('second smallest:',x[1])
print('second greatest:',x[n-2])
a=0
for i in range (0,n-1):
    if x[i]%2==0:
        a=a+1
print('no of even no:',a)
