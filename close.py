a,b=[float(x)for x in input('enter the values:').split()]
z=a-b
if z<=0.001 or (-1*z)<=0.001:
    print('close')
else:
    print('not close')
    
