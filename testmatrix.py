#!/usr/bin/python3
import numpy as np
x=[]
frac=[]
'''n=int(input("enter number of elements"))
print("enter elements")
for i in range(0,n):
	a=int(input("enter element"))
	x.append(a)
'''

while True:
	try:
		a=int(input())
		x.append(a)
	except:
		break;
	
#print (x)
length=len(x)
#print (length)
for  i in range(1,length+1):
	if(length%i==0):
		frac.append(i)
#print (frac)
mat=np.array(x)
#print (mat)

lengthf=len(frac)
print (lengthf)

for i in range(0,lengthf):
	x=length/frac[i]
	y=mat.reshape(frac[i],int(x))
	print ("matrix number:  "+str(i+1))
	print (y)
	print (y.shape)

	


		
